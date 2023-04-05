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
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)
    
    @name.default
    def _(self) -> str:
        return f"({'|'.join(map(str, self.rules))})"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        for rule in self.rules[:-1]:
            if (yield rule).match:
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
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)

    @name.default
    def _(self) -> str:
        return f"{self.rule}+"

    def grammar(self) -> Grammar:
        yield self.rule
        yield Action.OPTIONAL
        while (yield self.rule).match: ...

@define
class ZeroOrMore(Rule):
    """Match a rule zero or more times."""
    
    rule: Rule
    """The rule to match."""
    name: str = field()
    """The name of the rule."""
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)

    @name.default
    def _(self) -> str:
        return f"{self.rule}*"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        while (yield self.rule).match: ...

@define
class Repeat(Rule):
    """Matches a rule ``n`` timrs."""

    rule: Rule
    """The rule to match."""
    amount: int
    """The amount of repetitions to match."""
    name: str = field()
    """The name of the rule."""
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)

    @name.default
    def _(self) -> str:
        return f"{self.rule}{{n}}"

    def grammar(self) -> Grammar:
        matches = 0
        while matches < self.amount and (yield self.rule):
            matches += 1
        if matches < self.amount:
            yield Action.NO_MATCH

@define
class Optional(Rule):
    """Optionally match a rule."""
    
    rule: Rule
    """The rule to match."""
    name: str = field()
    """The name of the rule."""
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)
    
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
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)

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
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)
    
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
    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=False)

    @name.default
    def _(self) -> str:
        return f"!{self.rule}"
    
    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        res = yield self.rule
        yield Action.REQUIRE
        if res.consumed_all:
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
    res = yield Any()
    yield Action.REQUIRE
    if res.match:
        yield Action.NO_MATCH

@rule(name = "ASCII digit", silent_children=False)
def AsciiDigit() -> Grammar:
    """
    Matches any ASCII digit.
    """
    yield RuleUnion(list(map(String, stringlib.digits)))

@rule(name = "ASCII letter", silent_children=False)
def AsciiLetter() -> Grammar:
    """
    Matches any ASCII letter.
    """
    yield RuleUnion(list(map(String, stringlib.ascii_letters)))

@rule(name = "ASCII lowercase letter", silent_children=False)
def AsciiLowercase() -> Grammar:
    """
    Matches any ASCII lowercase letter.
    """
    yield RuleUnion(list(map(String, stringlib.ascii_lowercase)))

@rule(name = "ASCII uppercase letter", silent_children=False)
def AsciiUppercase() -> Grammar:
    """
    Matches any ASCII uppercase letter.
    """
    yield RuleUnion(list(map(String, stringlib.ascii_uppercase)))

@rule(name = "HEX digit", silent_children=False)
def HexDigit() -> Grammar:
    """
    Matches any hexadecimal digit.
    """
    yield RuleUnion(list(map(String, stringlib.hexdigits)))

@define
class String(Rule):
    """Match a string."""
    
    string: str
    """The string to match."""
    case_sensitive: bool = field(kw_only=True, default=True)
    """Differs between upper and lower case."""
    name: str = field(kw_only=True)
    """The name of the rule."""

    silent: bool = field(init=False, default=False)
    silent_children: bool = field(init=False, default=True)

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


