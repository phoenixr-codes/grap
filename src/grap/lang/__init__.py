from __future__ import annotations

from pathlib import Path
from attrs import define

from grap.core.parser import parse

from . import grammar


@define
class Parser:
    grammar: str

    @classmethod
    def from_path(cls, path: Path) -> Parser:
        return cls(path.read_text())
    
    def __attrs_post_init__(self) -> None:
        # TODO
        ...
