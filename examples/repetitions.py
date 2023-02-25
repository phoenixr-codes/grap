"""
Example demonstrating how to use repeating
rules.
"""

from __future__ import annotations

from grap.core.common import String, ZeroOrMore, OnceOrMore, Optional
from grap.core.rules import Grammar, rule

@rule
def main() -> Grammar:
    yield Optional(String("a"))
    yield OnceOrMore(String("b"))
    yield ZeroOrMore(String("c"))