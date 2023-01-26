from __future__ import annotations

from abc import ABC, abstractmethod
from .action import Action
from .errors import ParseError

class Rule(ABC):
    def __init__(self, name: Optional[str] = None):
        self.name = name
        self._inner: list[Rule] = list()
    
    def __or__(self, other: Rule) -> RuleUnion:
        return RuleUnion([self, other], operate = any)
    
    def __and__(self, other: Rule) -> RuleUnion:
        return RuleUnion([self, rule], operate = all)
    
    @property
    def inner(self) -> list[Rule]:
        return self._inner
    
    @abstractmethod
    def expect(self) -> Generator[Rule | RuleUnion]:
        ...

class RuleUnion(Rule):
    def __init__(
        self,
        rules: list[Rule] = None,
        operate: Literal[any] | Literal[all] = None,
    ):
        self.rules = rules
        self.operate = operate
        super().__init__()
    
    def __or__(self, other: Rule) -> RuleUnion:
        return RuleUnion([*self, other], operate = any)
    
    def __and__(self, other: Rule) -> RuleUnion:
        return RuleUnion([*self, other], operate = all)
    
    def expect(self):
        if self.operate == any:
            for r in self.rules[:-1]:
                yield r, True
                yield Action.GO_BACK
            yield self.rules[-1], True
        else:
            raise NotImplementedError()

class String(Rule):
    def __init__(self, string: str, case_sensitive: bool = True):
        self.string = string
        self.case_sensitive = case_sensitive
        super().__init__()
    
    def expect(self):
        for char in self.string:
            if self.case_sensitive:
                yield char
            else:
                yield String(char.upper()) | String(char.lower())
