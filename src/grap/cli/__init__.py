"""
The CLI for grap.
"""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from importlib import import_module
from importlib.metadata import version
import sys
from typing import Optional

from grap import core, lang
from loguru import logger
from rich import print as rprint

ap = ArgumentParser(prog="grap")

ap.add_argument(
    "-V", "--version",
    action="version",
    version=f"%(prog)s v{version('grap')}"
)

ap.add_argument(
    "-v", "--verbose",
    help="Enables logging. Repeat this flag up to 6 times to increase the logging level.",
    action="count",
    default=0
)

ap.add_argument(
    "grammar",
    help="The path to the grammar file.",
    type=Path
)

ap.add_argument(
    "text",
    help="The text to parse.",
)

ap.add_argument(
    "-f", "--fromfile",
    help="Use the `text` argument as a path instead of reading from the command-line.",
    action="store_true",
    default=False
)

ap.add_argument(
    "--raw",
    help="Disables pretty output.",
    action="store_true",
    default=False
)

ap.add_argument(
    "-t", "--type",
    help="Specify the file type of the grammar. When this is `auto` (default) the file type is assumed by its extension",
    choices=["auto", "python", "grap"],
    default="auto"
)

ap.add_argument(
    "-r", "--rule",
    help="The name of the rule to parse the text with.",
    default="main",
    metavar="NAME"
)

def parse(with_args: Optional[list[str]] = None) -> None:
    args = ap.parse_args(with_args)
    
    assert args.verbose < 7, "verbose level to high"

    logger.remove()
    logger.enable("grap.core.parser")
    logger.add(sys.stderr, level=[
        "CRITICAL",
        "ERROR",
        "WARNING",
        "SUCCESS",
        "INFO",
        "DEBUG",
        "TRACE",
    ][args.verbose])
        

    grammar = args.grammar
    if args.fromfile:
        text = Path(args.text).read_text()
    else:
        text = args.text
    rule_name = args.rule

    kind = args.type
    if kind == "auto":
        suffix = args.grammar.suffix
        if suffix == ".py":
            kind = "python"
        elif suffix == ".grap":
            kind = "grap"
        else:
            raise RuntimeError(f"invalid file extension {suffix!r} for automatic detection")
    
    if kind == "python":
        sys.path.append(str(grammar.resolve().parent))
        mod = import_module(str(grammar.stem))
        rule = getattr(mod, rule_name)
        result = core.parse(rule(), text)
    elif kind == "grap":
        result = lang.Parser.from_path(grammar).parse(rule_name, text)
    
    if args.raw:
        print(result)
    else:
        rprint(result)

    sys.exit(0)
