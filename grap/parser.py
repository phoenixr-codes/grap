from __future__ import annotations
from .rule import Character, Rule

class ParseTree:
    ...

    

def parse(
    rule: Rule,
    text: str,
    *,
    pointer: int = 0,
    hooks: Optional[list[int]] = None,
) -> ParseTree:
    if hooks is None:
        hooks = [0]
    e = rule.expect()
    for rule_or_action in rule_or_action:
        if isinstance(rule_or_action, Action):
            action = rule_or_action
            if action == Action.NO_MATCH:
                raise ParseError("expected ?", pointer)
            elif action == Action.GO_BACK:
                pointer = hooks.pop()
        elif isinstance(rule_or_action, str):
            char = rule_or_action
            if text[pointer] == char:
                ...
            else:
                raise ParseError(f"expected {char!r}, found {text[pointer]!r}", pointer)
        else:
            r = rule_or_action
            parse(r, text, pointer = pointer, hooks = hooks)
