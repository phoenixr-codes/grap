from __future__ import annotations

from collections.abc import Generator
from functools import partial
from typing import Optional

from attrs import define, Factory, field
from loguru import logger

from .action import Action
from .errors import ParseError
from .rules import Rule


logger.disable(__name__)

def parse(rule: Rule, text: str) -> ParsedRule:
    pr, pointer, consumed = _parse_rule(rule, text)
    assert consumed
    assert len(text) - 1 < pointer # not all characters were consumed
    return pr

@define(kw_only = True)
class ParsedRule:
    name: str
    rule: Rule
    match: str
    span: tuple[int, int]
    parent: Optional[ParsedRule] = None
    inner: list[Rule] = field(default = Factory(list))
    
    def parents(self) -> Generator[ParsedRule, None, None]:
        p = self.parent
        while p is not None:
            yield p
            p = p.parent

def _parse_rule(
    rule: Rule,
    text: str,
    *,
    pointer: int = 0,
    hooks: Optional[list[int]] = None,
    parents: Optional[list[ParsedRule]] = None,
    all_optional: bool = False,
) -> tuple[ParsedRule, int]:
    if hooks is None: hooks = [pointer]
    if parents is None: parents = []
    
    grammar = rule.grammar()
    
    optional = all_optional
    inner = []
    consumed: Optional[bool] = None
    any_consumed: bool = False
    
    pr = partial(
        ParsedRule,
        name = rule.name,
        rule = rule,
        parent = None if not parents else parents[-1],
        inner = inner,
    )
    
    try:
        while True:
            if consumed:
                any_consumed = True
            rule_or_action = grammar.send(consumed)
            consumed = None
            
            logger.debug(f"{str(rule_or_action) = }")
            
            if rule_or_action == Action.GO_BACK:
                previous = hooks.pop()
                logger.debug(f"pointer goes back from {pointer} to {previous}")
                pointer = previous
            elif rule_or_action == Action.NO_MATCH:
                if not optional:
                    raise ParseError("did not match", pointer)
                consumed = False
            elif rule_or_action == Action.IS_MATCH:
                logger.debug("forced consuming char")
                try:
                    char = text[pointer]
                except IndexError:
                    if not optional:
                        raise ParseError("EOF reached", pointer)
                    else:
                        consumed = False
                        continue
                consumed = True
                hooks.append(pointer)
                pointer += 1
                logger.debug("moved pointer by 1")
            elif rule_or_action == Action.OPTIONAL:
                optional = True
                logger.debug("made rules optional")
            
            elif rule_or_action == Action.REQUIRE:
                if all_optional:
                    logger.debug("encountered REQUIRE but suppressing it")
                else:
                    optional = False
                    logger.debug(f"made rules mandatory for rule {rule} and its subrules")
            
            elif isinstance(rule_or_action, str):
                char = rule_or_action
                logger.debug(f"checking for character {char!r}")
                try:
                    got = text[pointer]
                except IndexError:
                    if not optional:
                        raise ParseError(f"expected {char!r}, got EOF", pointer)
                    else:
                        consumed = False
                        continue
                if char == got:
                    logger.debug(f"character {char!r} matches")
                    consumed = True
                    hooks.append(pointer)
                    pointer += 1
                    logger.debug("moved pointer by 1")
                else:
                    logger.debug(f"character {char!r} does not match {got!r}")
                    if not optional:
                        raise ParseError(
                            f"expected {char!r}, got {got!r}", pointer
                        )
                    consumed = False
            elif isinstance(rule_or_action, Rule):
                logger.debug(f"parsing subrule {rule_or_action} of {rule}")
                pr_sub, pointer, consumed = _parse_rule(
                    rule_or_action,
                    text,
                    pointer = pointer,
                    #hooks = hooks,
                    parents = [*parents, rule_or_action],
                    all_optional = optional,
                )
                if consumed:
                    inner.append(pr_sub)
            
            else:
                raise TypeError(
                    f"invalid object {rule_or_action!r} of type "
                    f"{type(rule_or_action)!r}"
                )
    except StopIteration:
        pass
    
    span = (hooks[-1], pointer - 1)
    pr = pr(match = text[slice(*span)], span = span)
    return pr, pointer, any_consumed
