**********
Quickstart
**********

Installation
************

You can install ``grap`` with ``pip``:

.. code-block:: bash
    
    python -m pip install grap[dev]

Write a Basic Grammar
*********************

Let's write a basic grammar for a mathematical expression parser.

.. code-block:: python
    
    from grap.core.rules import rule
    from grap.core.common import AsciiDigit, OnceOrMore, Optional, RuleUnion
    
    @rule
    def main():
        yield OnceOrMore(AsciiDigit())
        yield Optional(whitespace())
        yield operator()
        yield Optional(whitespace())
        yield OnceOrMore(AsciiDigit())
    
    @rule
    def whitespace():
        yield OnceOrMore(" ")
    
    @rule
    def operator():
        yield RuleUnion(("+", "-", "*", "/"))


Save this file as ``math_expr.py``.

Parse Text
**********

After you have saved the gramar file you are able to parse text with it.
Use the python REPL in the same directory as your grammar file.

.. repl::
    
    from grap.core import parse
    from rich import print
    
    #repl:hide-output
    from math_expr import main
    #repl:hide
    from grap.core.rules import rule
    from grap.core.common import AsciiDigit, OnceOrMore, Optional, RuleUnion
    
    @rule
    def main():
        yield OnceOrMore(AsciiDigit())
        yield Optional(whitespace())
        yield operator()
        yield Optional(whitespace())
        yield OnceOrMore(AsciiDigit())
    
    @rule
    def whitespace():
        yield OnceOrMore(" ")
    
    @rule
    def operator():
        yield RuleUnion(("+", "-", "*", "/"))
    
    #repl:show
    
    
    print(parse(main(), "42 - 7"))

This will print a large parse tree. Instead of writing a seperate script,
you may instead use the command line interface of grap to quickly parse
text.

.. code-block:: bash
    
    python -m grap math_expr.py "42 - 7"

This will look for a rule named ``'main'`` in the file ``math_expr.py``
and parse the text ``"42 - 7"``. To learn more read the documentation
of  the `CLI <cli>`_.

