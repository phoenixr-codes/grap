"""
Example explaining repeating rules.
"""

from __future__ import annotations

from grap.core.common import *
from grap.core.rules import Grammar, rule

@rule
def main() -> Grammar:
    yield String("(")
    yield five_a()
    yield String(")")

@rule
def five_a() -> Grammar:
    yield Repeat(String("a", case_sensitive=False), 5)
