***********
Cheat Sheet
***********

Rules
*****

.. code-block:: grap
    
    [rule_name]
    (a | b)+
    
    :[silent_rule]:
    (a | b)+

Syntax
******

=======
``a b``
=======

``a`` followed by ``b``.

========
``a, b``
========

``a`` followed by ``Seperator`` followed by ``b``. This is the same as ``a, Seperator, b``.

========
``a; b``
========

``a`` optionally followed by ``Seperator`` followed by ``b``. This is the same as ``a, Seperator?, b``.

========================================================
``// single-line comment``, ``/* multi-line comment */``
========================================================

Comments are ignored by the parser. They are usually used to explain parts of the document or temporarily disable
rules.

=========
``a | b``
=========

``a`` or ``b``.

==========
``a & b``
==========

``a`` as well as ``b``.

=========
``!a, b``
=========

Not ``a`` but ``b``.

======
``a*``
======

``a`` zero or more times.

======
``a+``
======

``a`` one or more times.

======
``a?``
======

``a`` zero times or once.

========
``a{n}``
========

``a`` exactly ``n`` times.

==========
``a{n..}``
==========

``a`` at least ``n`` times.

==========
``a{..m}``
==========

``a`` at most ``m`` times``.

===========
``a{n..m}``
===========

``a`` between ``n`` and ``m`` times.

============
``"a"-"f"``
============

Lowercase letter between ``"a"`` and ``"f"``.

===========
``"0"-"5"``
===========

Digit between ``"0"`` and ``"5"``.

================
``x<a+>, b{#x}``
================

``a`` once or more times followed by ``b`` repeating the amount of repetitions of ``a``.

================
``x<a+>, b, $x``
================

``a`` once or more times followed by ``b`` followed by the first match.

Statements
**********

All statements must come before any rule is defined.

==========
``load f``
==========

Loads all rules from another grammar in the same directory. ``f`` must match the file name without its extension.
For a file in a subdirectory use a "/" and for files in a parent directory use "../".

=================
``load r from f``
=================

Loads rule ``r`` from grammar file ``f``.

Predefined Rules
****************

============
ASCII_LETTER
============

Matches any ASCII letter.

===============
ASCII_LOWERCASE
===============

Matches any lowercase ASCII letter (a-z).
