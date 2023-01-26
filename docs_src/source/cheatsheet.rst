.. |yes| replace:: |:heavy_check_mark:|
.. |no| replace:: |:x:|

***********
Cheat Sheet
***********

Rules
*****

.. code-block:: grap
    
    [rule_name]
    /// Optional Doc-Block describing the rule.
    (a| b)+
    

----

Syntax
******

=======
``a b``
=======

``a`` followed by ``b``.

----

========
``a, b``
========

``a`` followed by ``Seperator`` followed by ``b``. This is the same as ``a Seperator b``.

Examples
========

.. code-block::
    
    [Seperator]
    whitespace
    
    [whitespace]
    " "+

------------
``"a", "b"``
------------

* |no| ``ab``
* |yes| ``a b``
* |yes| ``a  b``

----

========
``a; b``
========

``a`` optionally followed by ``Seperator`` followed by ``b``. This is the same as
``a Seperator? b``.

Examples
========

.. code-block::
    
    [Seperator]
    whitespace
    
    [whitespace]
    " "+

------------
``"a"; "b"``
------------

* |yes| ``ab``
* |yes| ``a b``
* |yes| ``a  b``

----

========================================================
``// single-line comment``, ``/* multi-line comment */``
========================================================

Comments are ignored by the parser. They are usually used to explain parts of the document
or temporarily disable rules.

Examples
========

.. code-block:: grap
    
    // The following line loads an awesome rule.
    load awesome_rule from foo

----

=================
``/// Doc-Block``
=================

Doc-Blocks are a special type of comment. When they immediatly follow are rule definition
they are used as a docstring for the python rule that is generated. Unlike in most programming
languages, there is no way of using a Doc-Block with multi-line comments.

You may as well use them at the top of the document to describe the grammar file and/or
specify the author, the version or other such things.

Examples
========

.. code-block:: grap
    
    /// This grammar file contains the main part.
    
    load barely from foo
    load anything from bar
    
    [rule]
    /// This Doc-Block precisely explains what this rule is
    /// and does.
    barely | anything

----

=========
``a | b``
=========

``a`` or ``b``.

Examples
========

-------------
``"X" | "Y"``
-------------

* |yes| ``X``
* |yes| ``Y``
* |no| ``XY``
* |no| ``XX``
* |no| ``YY``

-------------------
``"X" | "Y" | "Z"``
-------------------

* |yes| ``X``
* |yes| ``Y``
* |yes| ``Z``

----

========
``&a b``
========

``a`` as well as ``b``.

Examples
========

--------------------
``&("X" | "Y") "X"``
--------------------

* |yes| ``X``
* |no| ``Y``

----

========
``!a b``
========

Not ``a`` but ``b``.

----

======
``a*``
======

``a`` zero or more times.

Examples
========

------------
``"X" "Y"*``
------------

* |yes| ``X``
* |yes| ``XY``
* |yes| ``XYY``
* |yes| ``XYYY``

----

======
``a+``
======

``a`` one or more times.

Examples
========

------------
``"X" "Y"+``
------------

* |no| ``X``
* |yes| ``XY``
* |yes| ``XYY``
* |yes| ``XYYY``

----

======
``a?``
======

``a`` zero times or once.

Examples
========

------------
``"X" "Y"?``
------------

* |yes| ``X``
* |yes| ``XY``
* |no| ``XYY``
* |no| ``XYYY``

----

========
``a{n}``
========

``a`` exactly ``n`` times.

Examples
========

----------
``"X"{3}``
----------

* |no| ``X``
* |no| ``XX``
* |yes| ``XXX``
* |no| ``XXXX``

----

==========
``a{n..}``
==========

``a`` at least ``n`` times.

Example
=======

------------
``"X"{3..}``
------------

* |no| ``X``
* |no| ``XX``
* |yes| ``XXX
* |yes| ``XXXX``
* |yes| ``XXXXX``

----

==========
``a{..m}``
==========

``a`` at most ``m`` times``.

Examples
========

----------------
``"X"{..3} "Y"``
----------------

* |yes| ``Y``
* |yes| ``XY``
* |yes| ``XXY``
* |yes| ``XXXY``
* |no| ``XXXXY``
* |no| ``XXXXXY``

----

===========
``a{n..m}``
===========

``a`` between ``n`` and ``m`` times.

Examples
========

-------------
``"X"{2..4}``
-------------

* |no| ``X``
* |yes| ``XX``
* |yes| ``XXX``
* |yes| ``XXXX``
* |no| ``XXXXX``

----

=========
``"abc"``
=========

The string ``"abc"``.

----

============
``"a"-"f"``
============

Lowercase letter between ``"a"`` and ``"f"``.

Examples
========

-----------
``"b"-"e"``
-----------

* |no| ``a``
* |yes| ``b``
* |no| ``B``
* |yes| ``c``
* |yes| ``d``
* |yes| ``e``
* |no| ``f``

----

===========
``"0"-"5"``
===========

Digit between ``"0"`` and ``"5"``.

----

=================
``x=(a+), b{#x}``
=================

``a`` once or more times followed by ``b`` repeating the amount of repetitions of ``a``.

----

=================
``x=(a+), b, $x``
=================

``a`` once or more times followed by ``b`` followed by the first match.

----

========
``a<x>``
========

``a`` named ``x``. This only effects error messages and may be used to give the rule a better
name depending on the context.

----

Statements
**********

All statements must appear before any rule is defined.

=================
``load * from f``
=================

Loads all rules except context rules from another grammar in the same directory. ``f``
must match the file name without its extension. For a file in a subdirectory use a "/"
and for files in a parent directory use "../".

----

=================
``load r from f``
=================

Loads rule ``r`` from grammar file ``f``.

----

====================
``load r, s from f``
====================

Loads rule ``r`` and ``s`` from grammar file ``f``.

----

======================
``load r as x from f``
======================

Loads rule ``r`` from grammar file ``f`` and rename it to ``x``.

----

Predefined Rules
****************

.. todo:: Sort these.

============
ASCII_LETTER
============

Matches any ASCII letter.

----

===============
ASCII_LOWERCASE
===============

Matches any lowercase ASCII letter (a-z).

----

===============
ASCII_UPPERCASE
===============

Matches any uppercase ASCII letter (A-Z).

----

===========
ASCII_DIGIT
===========

Matches any ASCII digit (0-9).
