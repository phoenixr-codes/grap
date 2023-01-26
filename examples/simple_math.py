r"""
Example of a parser for a simple math expression.
The equivalent regular expression would be ``\d+ *(\+|-|\*|/) *\d+``.
"""

from __future__ import annotations
from grap.core.common import *
from grap.core.rules import Grammar, rule

@rule
def main() -> Grammar:
    yield number()
    yield Optional(whitespace())
    yield operator()
    yield Optional(whitespace())
    yield number()

@rule
def digit() -> Grammar:
    yield RuleUnion(
        String("0"),
        String("1"),
        String("2"),
        String("3"),
        String("4"),
        String("5"),
        String("6"),
        String("7"),
        String("8"),
        String("9"),
    )

@rule
def whitespace():
    yield OnceOrMore(" ")

@rule
def number() -> Grammar:
    yield OnceOrMore(digit())

@rule
def operator() -> Grammar:
    yield RuleUnion(
        String("+"),
        String("-"),
        String("*"),
        String("/"),
    )

if __name__ == "__main__":
    from argparse import ArgumentParser, FileType
    import sys
    
    try:
        from rich import print
    except ModuleNotFoundError:
        from warnings import warn
        warn("you may wish to installe the `rich` library for better output", RuntimeWarning)
        #from pprint import pprint
    from grap.core.parser import parse
    
    ap = ArgumentParser()
    ap.add_argument("-f", type = FileType("w"), default = sys.stdout)
    args = ap.parse_args()
    
    print(parse(main(), "1 + 1"), file = args.f)
    print(parse(main(), "69  *420"), file = args.f)
