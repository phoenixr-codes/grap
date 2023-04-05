"""
Example demonstrating the error message that occures when
parentheses were forgotten after a rule.
"""

from __future__ import annotations

from grap.core.common import Any
from grap.core.rules import Grammar, rule

@rule
def main() -> Grammar:
    yield Any  # type: ignore
