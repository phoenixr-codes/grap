from __future__ import annotations

from attrs import define, field

from .action import Action
from .rules import Grammar, Rule, rule

class RuleUnion(Rule):
    def __init__(
        self,
        *rules: Rule,
    ):
         self.rules = rules
         super().__init__(name = "|".join(map(str, rules)))

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
    rule: Rule
    name: str = field()

    @name.default
    def _(self):
        return f"{self.rule}+"

    def grammar(self) -> Grammar:
        yield self.rule
        yield Action.OPTIONAL
        while (yield self.rule): ...

@define
class ZeroOrMore(Rule):
    rule: Rule
    name: str = field()

    @name.default
    def _(self):
        return f"{self.rule}*"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        while (yield self.rule): ...

@define
class Optional(Rule):
    rule: Rule
    name: str = field()

    @name.default
    def _(self):
        return "{self.rule}?"

    def grammar(self) -> Grammar:
        yield Action.OPTIONAL
        yield self.rule

@rule(name = "ASCII Digit")
def AsciiDigit():
    yield RuleUnion(*(String(str(x)) for x in range(10)))

class String(Rule):
    def __init__(
        self,
        string: str,
        case_sensitive: bool = True,
    ):
        self.string = string
        self.case_sensitive = case_sensitive
        super().__init__(name = repr(string) + "" if case_sensitive else "i")

    def grammar(self) -> Grammar:
        for char in self.string:
            if self.case_sensitive:
                yield char
            else:
                yield RuleUnion(
                    self.__class__(char.upper()),
                    self.__class__(char.lower())
                )


