from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from .action import Action

@dataclass
class Rule(ABC):
    name: Optional[str] = None
    
    def __or__(self, other: Rule | RuleUnion) -> RuleUnion:
        rules = [self]
        rules.extend(other)
        return RuleUnion(rules, operate = any)
    
    def __and__(self, other: Rule | RuleUnion) -> RuleUnion:
        rules = [self]
        rules.extend(other)
        return RuleUnion(rules, operate = all)
    
    @abstractmethod
    def expect(self) -> Generator[Rule | RuleUnion]:
        ...

@dataclass
class RuleUnion(Rule):
    rules: Iterable[Rule]
    operate: Callable[[Iterable[Rule]], bool]
    
    def __post_init__(self):
        self.rules = flatten(self.rules)
    
    def expect(self):
        for r in self.rules:
            result = yield r
            if result.success:
                break
            else:
                yield Action.GO_BACK
        else:
            yield Action.NO_MATCH
