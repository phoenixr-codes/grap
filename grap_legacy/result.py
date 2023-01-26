from __future__ import annotations

class Result:
    def __init__(self, value: T):
        self._value = value
    
    @property
    def value(self) -> T:
        return self._value
    
    def unwrap(self) -> T:
        if isinstance(self._value, BaseException):
            raise self._value
        return self._value
