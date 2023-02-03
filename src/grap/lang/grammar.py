# TODO: sort alphabetical

from __future__ import annotations

from grap.core.common import (
    Any,
    AsciiDigit,
    AsciiLetter,
    Chained,
    End,
    NegativePredicate,
    OnceOrMore,
    Optional,
    RuleUnion,
    String,
    ZeroOrMore,
)
from grap.core.rules import Grammar, rule

@rule
def main() -> Grammar:
    yield ZeroOrMore(statement())
    #yield ZeroOrMore(rules())

@rule
def statement() -> Grammar:
    yield load()

@rule
def load() -> Grammar:
    yield String("load")
    yield whitespace()
    yield RuleUnion([identifier(), wildcard()])
    yield whitespace()
    yield String("from")
    yield whitespace()
    yield identifier()

@rule
def grammar() -> Grammar:
    yield Optional(predicate())
    yield identifier()
    yield Optional(modifier())

@rule
def rule_def() -> Grammar:
    yield String("[")
    yield identifier()
    yield String("]")

@rule
def singleline_comment() -> Grammar:
    yield String("//")
    yield Chained([
        NegativePredicate(End()),
        NegativePredicate(String("\n")),
        Any()
    ])
    yield RuleUnion([End(), String("\n")])

@rule
def multiline_comment() -> Grammar:
    yield String("/*")
    yield Chained([
        NegativePredicate()
    ])

@rule
def modifier() -> Grammar:
    yield RuleUnion([
        mod_zero_or_more(),
        mod_once_or_more(),
        mod_optional(),
        mod_repeat(),
    ])

@rule
def mod_zero_or_more() -> Grammar:
    yield String("*")

@rule
def mod_once_or_more() -> Grammar:
    yield String("+")

@rule
def mod_optional() -> Grammar:
    yield String("?")

@rule
def mod_repeat() -> Grammar:
    yield String("{")
    yield Optional(whitespace())
    yield RuleUnion([
        Chained([number(), String(".."), number()]),
        Chained([number(), String("..")]),
        Chained([String(".."), number()]),
    ])
    yield Optional(whitespace())
    yield String("}")

@rule
def chain() -> Grammar:
    yield RuleUnion([
        String(","),
        String(";"),
        String("|"),
    ])

@rule
def predicate() -> Grammar:
    yield RuleUnion([String("&"), String("!")])

@rule
def number() -> Grammar:
    yield OnceOrMore(AsciiDigit())

@rule
def identifier() -> Grammar:
    yield OnceOrMore(
        RuleUnion([AsciiLetter, AsciiDigit, String("_")])
    )

@rule
def whitespace() -> Grammar:
    yield OnceOrMore(RuleUnion([
        String(" "),
        String("\n"),
        String("\t")
    ]))

@rule
def wildcard() -> Grammar:
    yield String("*")