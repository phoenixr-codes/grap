from __future__ import annotations

from collections.abc import Sequence
import string as stringlib

from attrs import define, field

from .action import Action
from .rules import Grammar, Rule, rule

@define
class RuleUnion(Rule):
    """Match one of multiple rules."""
    
    rules: Sequence[Rule]
    """The rules to match."""
    name: str = field()
    """The name of the rule."""
    
    @name.default
    def _(self) -> str:
        return f"({'|'.join(map(str, self.rules))})"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        for rule in self.rules[:-1]:
            if (yield rule):
                break
        else:
            yield Action.REQUIRE
            yield self.rules[-1]

@define
class OnceOrMore(Rule):
    """Match a rule one or more times."""
    
    rule: Rule
    """The rule to match."""
    name: str = field()
    """The name of the rule."""

    @name.default
    def _(self) -> str:
        return f"{self.rule}+"

    def grammar(self) -> Grammar:
        yield self.rule
        yield Action.OPTIONAL
        while (yield self.rule): ...

@define
class ZeroOrMore(Rule):
    """Match a rule zero or more times."""
    
    rule: Rule
    """The rule to match."""
    name: str = field()
    """The name of the rule."""

    @name.default
    def _(self) -> str:
        return f"{self.rule}*"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        while (yield self.rule): ...

@define
class Optional(Rule):
    """Optionally match a rule."""
    
    rule: Rule
    """The rule to match."""
    name: str = field()
    """The name of the rule."""
    
    @name.default
    def _(self) -> str:
        return f"{self.rule}?"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        yield self.rule

@define
class Chained(Rule):
    """
    Matches all rules in a row.
    """

    rules: list[Rule]
    """The rules to match."""
    name: str = field()
    """The name of the rule."""

    @name.default
    def _(self) -> str:
        return " -> ".join(map(str, self.rules))
    
    def grammar(self) -> Grammar:
        for r in self.rules:
            yield r

@define
class PositivePredicate(Rule):
    """
    Matches a rule without consuming it.
    """

    rule: Rule
    """The rule to match."""
    name: str = field()
    """The name of the rule."""
    
    @name.default
    def _(self) -> str:
        return f"&{self.rule}"
    
    def grammar(self) -> Grammar:
        yield self.rule
        yield Action.GO_BACK

@define
class NegativePredicate(Rule):
    """
    Matches when the rule is not present without consuming it.
    """

    rule: Rule
    """The rule to not match."""
    name: str = field()
    """The name of the rule."""

    @name.default
    def _(self) -> str:
        return f"!{self.rule}"
    
    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        consumed = yield self.rule
        yield Action.REQUIRE
        if consumed:
            yield Action.NO_MATCH
            yield Action.GO_BACK

@rule(name = "Any character")
def Any() -> Grammar:
    """
    Matches any character.
    """
    yield Action.IS_MATCH

@rule
def End() -> Grammar:
    """
    Matches when the end of the input is reached.
    """
    yield Action.OPTIONAL
    consumed = yield Any()
    yield Action.REQUIRE
    if consumed:
        yield Action.NO_MATCH

@rule(name = "ASCII digit")
def AsciiDigit() -> Grammar:
    """
    Matches any ASCII digit.
    """
    yield RuleUnion(list(map(String, stringlib.digits)))

@rule(name = "ASCII letter")
def AsciiLetter() -> Grammar:
    """
    Matches any ASCII letter.
    """
    yield RuleUnion(list(map(String, stringlib.ascii_letters)))

@rule(name = "ASCII lowercase letter")
def AsciiLowercase() -> Grammar:
    """
    Matches any ASCII lowercase letter.
    """
    yield RuleUnion(list(map(String, stringlib.ascii_lowercase)))

@rule(name = "ASCII uppercase letter")
def AsciiUppercase() -> Grammar:
    """
    Matches any ASCII uppercase letter.
    """
    yield RuleUnion(list(map(String, stringlib.ascii_uppercase)))

@rule(name = "HEX digit")
def HexDigit() -> Grammar:
    """
    Matches any hexadecimal digit.
    """
    yield RuleUnion(list(map(String, stringlib.hexdigits)))

@define
class String(Rule):
    """Match a string."""
    
    string: str
    case_sensitive: bool = field(kw_only=True, default=True)
    name: str = field(kw_only=True)

    @name.default
    def _(self) -> str:
        return repr(self.string) + ("" if self.case_sensitive else "i")
    
    def grammar(self) -> Grammar:
        for char in self.string:
            if self.case_sensitive:
                yield char
            else:
                yield RuleUnion((
                    self.__class__(char.upper()),
                    self.__class__(char.lower())
                ))


