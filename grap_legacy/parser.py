from __future__ import annotations

from itertools import count

from loguru import logger

from .action import Action
from .errors import ParseError
from .rule import Rule

def unpack(value: T, default: bool = False) -> tuple[T, bool]:
    if isinstance(value, tuple):
        return value
    else:
        return value, default

def parse(rule: Rule, text: str) -> Rule:
    return parse_engine(rule, text)[0]

def parse_engine(
    rule: Rule,
    text: str,
    *,
    pointer: int = 0,
    hooks: Optional[list[int]] = None,
    root: bool = True,
    skip: bool = False,
) -> Rule:
    if hooks is None:
        hooks = [0]
    result = None
    e = rule.expect()
    try:
        for subsequent in count(0):
            rule_or_action, skip = unpack(e.send(None if subsequent else None), default = skip)
            result = None
            
            logger.debug(f"{skip = }")
            
            if isinstance(rule_or_action, Action):
                action = rule_or_action
                if action == Action.NO_MATCH:
                    err = ParseError("expected ?", pointer)
                    if not skip:
                        raise err
                elif action == Action.GO_BACK:
                    before = hooks.pop()
                    logger.debug(f"pointer goes back from {pointer} to {before}")
                    pointer = before
            
            elif isinstance(rule_or_action, str):
                char = rule_or_action
                logger.debug(f"try consuming {char!r} ...")
                if len(text) - 1 < pointer:
                    err = ParseError("EOF encountered", pointer)
                    if not skip:
                        raise err
                
                elif text[pointer] == char:
                    rule._inner.append(char)
                    hooks.append(pointer)
                    pointer += 1
                    logger.debug(f"consumed {char!r}")
                
                elif not skip:
                    raise ParseError(
                        f"expected {char!r}, found "
                        f"{text[pointer]!r} at {pointer}",
                        pointer,
                    )
            
            else:
                r = rule_or_action
                _, pointer = parse_engine(
                    r,
                    text,
                    pointer = pointer,
                    hooks = hooks,
                    root = False,
                    skip = skip,
                )
                rule._inner.append(r)
    
    except StopIteration:
        pass
    
    if root and (s := text[pointer:]):
        raise ParseError(f"expected EOF at {pointer}, found {s!r}", pointer)
    
    return rule, pointer
