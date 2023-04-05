from __future__ import annotations

from collections.abc import Generator
from functools import partial
from typing import Optional

from attrs import define, Factory, field
from loguru import logger

from .action import Action
from .errors import ParseError
from .rules import ParsedRule, ParseResult, Rule

logger.disable("grap.core.parser")

def parse(rule: Rule, text: str) -> ParsedRule:
    """
    Parameters
    ----------
    rule
        The rule to parse the text with.
    
    text
        The text to parse.
    
    Returns
    -------
    The parse tree.
    """
    tree, pointer, consumed = _parse_rule(rule, text)
    assert tree is not None
    assert consumed
    if len(text) - 1 >= pointer:
        raise ParseError(f"not all characters were consumed (expected EOF)", pointer)
    return tree



def _parse_rule(
    rule: Rule,
    text: str,
    *,
    pointer: int = 0,
    hooks: Optional[list[int]] = None,
    parents: Optional[list[Rule]] = None,
    all_optional: bool = False,
) -> tuple[Optional[ParsedRule], int, ParseResult]:
    """
    Returns
    -------
    A tuple containing the parsed rule, the new position of the
    pointer and the consumed characters as a string.
    """
    if hooks is None: hooks = [pointer]
    if parents is None: parents = []
    
    grammar = rule.grammar()
    
    optional: bool = all_optional
    inner: list[ParsedRule] = []
    any_consumed: bool = False
    all_consumed: bool = True
    consumed = ""
    
    partially_parsed_rule = partial(
        ParsedRule,
        name = rule.name,
        rule = rule,
        parent = None if not parents else parents[-1],
        inner = inner,
    )
    
    try:
        initial = True
        while True:
            if consumed:
                any_consumed = True
            else:
                all_consumed = False
            
            if initial:
                rule_or_action = next(grammar)
            else:
                rule_or_action = grammar.send(ParseResult(
                    match=consumed,
                    consumed_any=any_consumed,
                    consumed_all=all_consumed
                ))
            
            initial = False
            consumed = ""
            
            logger.debug(f"{str(rule_or_action) = }")
            
            if rule_or_action == Action.GO_BACK:
                previous = hooks.pop()
                logger.info(f"pointer goes back from {pointer} to {previous}")
                pointer = previous
            elif rule_or_action == Action.NO_MATCH:
                if not optional:
                    raise ParseError("did not match", pointer)
                consumed = ""
            elif rule_or_action == Action.IS_MATCH:
                logger.debug("forced consuming char")
                try:
                    char = text[pointer]
                except IndexError:
                    if not optional:
                        raise ParseError("EOF reached", pointer)
                    else:
                        consumed = ""
                        continue
                consumed = char
                hooks.append(pointer)
                pointer += 1
                logger.info(f"moved pointer by 1 (now at {pointer})")
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
                if len(char) != 1:
                    raise ParseError("expected char, got {char!r}", pointer)
                logger.debug(f"checking for character {char!r}")
                try:
                    got = text[pointer]
                except IndexError:
                    if not optional:
                        raise ParseError(f"expected {char!r}, got EOF", pointer)
                    else:
                        consumed = ""
                        continue
                if char == got:
                    logger.success(f"character {char!r} matches")
                    consumed = char
                    hooks.append(pointer)
                    pointer += 1
                    logger.info(f"moved pointer by 1 (now at {pointer})")
                else:
                    logger.info(f"character {char!r} does not match {got!r}")
                    if not optional:
                        raise ParseError(
                            f"expected {char!r}, got {got!r}", pointer
                        )
                    consumed = ""
            elif isinstance(rule_or_action, Rule):
                logger.debug(f"parsing subrule {rule_or_action} of {rule}")
                parsed_subrule, pointer, parse_result = _parse_rule(
                    rule_or_action,
                    text,
                    pointer = pointer,
                    #hooks = hooks,
                    parents = [*parents, rule_or_action],
                    all_optional = optional,
                )
                consumed = parse_result.match
                if consumed and not rule_or_action.silent_children:
                    assert parsed_subrule is not None
                    if not parsed_subrule.rule.silent:
                        inner.append(parsed_subrule)
            
            else:
                raise TypeError(
                    f"Invalid object {rule_or_action!r} of type "
                    f"{type(rule_or_action)!r}. Perhaps you forgot "
                    f"parentheses after the rule variable name?\n"
                    "`yield foo` -> `yield foo()`"
                )
    except StopIteration:
        pass
    
    if any_consumed:
        span = (0 if not hooks else hooks[-1], pointer) # - (1 if parents else 0))
        match = text[slice(*span)]
        parsed_rule = partially_parsed_rule(match = match, span = span)
    else:
        match = ""
        parsed_rule = None
    logger.success(f"successfully parsed rule {rule}: {match!r}")
    return parsed_rule, pointer, ParseResult(match=match, consumed_any=any_consumed, consumed_all=all_consumed)
