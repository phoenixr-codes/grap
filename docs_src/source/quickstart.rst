**********
Quickstart
**********

Installation
************

You can install ``grap`` with ``pip``:

.. code-block:: bash
    
    pip install grap

Write a Basic Grammar
*********************

Let's write a basic grammar for a mathematical expression parser.

.. code-block:: text
    
    [math_expr]
    (num | math_expr) (op (num | math_expr))*
    
    [op]
    "+" | "-" | "*" | "/"
    
    [num]
    ASCII_DIGIT+ ("." ASCII_DIGIT+)?

Save this document as ``math.grap``.

Generate the Parser
*******************

.. code-block:: bash
    
    grap build
