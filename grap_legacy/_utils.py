from __future__ import annotations

def flatten(it: Iterable[T]) -> Generator[T, None, None]:
    for i in it:
        if instance(i, (list, tuple)):
            yield from flatten(i)
        else:
            yield i
