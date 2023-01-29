**************************************************
Difference between ``grap.core`` and ``grap.lang``
**************************************************

The ``grap`` library contains two packages: :doc:`grap.core <../api-core>` and
:doc:`grap.lang <../api-lang>`. You can create grammar and parse text with both
packages. The major difference is that you define rules with ``grap.core``
**inside a python file** and ``grap.lang`` is **an own language**.

``grap.lang`` is generally prefered over ``grao.core``. ``grap.lang`` is written
with ``grap.core`` which could be seen as the low-level implementation.
