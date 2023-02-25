"""
Example demonstrating the usage of the
:class:`grap.core.common.Chained` rule.
"""

from __future__ import annotations

from grap.core.common import AsciiLetter, Chained, String
from grap.core.rules import Grammar, rule

@rule
def main() -> Grammar:
    yield Chained([String("abc"), AsciiLetter()])