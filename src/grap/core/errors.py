from __future__ import annotations

# TODO: @define (attrs will make sure this is a correct excecption class)

class ParseError(Exception):
    def __init__(self, message: str, location: int):
        self.message = message
        self.location = location
        super().__init__(message)

