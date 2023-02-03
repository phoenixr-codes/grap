"""
Example explaining predicating rules.
"""

from __future__ import annotations

from grap.core.common import *
from grap.core.rules import Grammar, rule

@rule
def a_to_f() -> Grammar:
    yield PositivePredicate(HexDigit())
    yield AsciiLowercase()

@rule
def comment() -> Grammar:
    yield String("/*")
    yield ZeroOrMore(Chained([
        NegativePredicate(String("*/")),
        Any()
    ]))
    yield String("*/")
