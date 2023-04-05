from __future__ import annotations

from abc import ABCMeta, abstractmethod
from collections.abc import Callable, Generator
import sys
from typing import Any, Optional, overload, TypeAlias, Union

from attrs import define, Factory, field

from .action import Action

Grammar: TypeAlias = "Generator[Union[Rule, Action, str], ParseResult, None]"

@define(kw_only=True)
class ParseResult:
    match: str
    consumed_any: bool
    consumed_all: bool

@define(kw_only = True)
class ParsedRule:
    """
    Attributes
    ----------
    name
        The name of the rule.
    
    rule
        The parsed rule object.
    
    match
        The consumed characters.
    
    span
        The index of the consumed characters in the parsed text.
    
    parent
        The parent rule. This is None when the rule is the root.
    
    inner
        All parsed subrules.
    
    """
    name: str
    rule: Rule
    match: str
    span: tuple[int, int]
    parent: Optional[Rule] = None
    inner: list[Rule] = field(default = Factory(list))

@define(init=False, slots=False)
class Rule(metaclass=ABCMeta):
    def __init__(
        self,
        name: Optional[str] = None,
        *,
        silent: bool = False,
        silent_children: bool = False,
    ):
        """
        Parameters
        ----------
        name
            The name of the rule. Defaults to the class's name.
        
        silent
            Excludes the rule from the parse tree when set to
            ``True``.
        
        silent_children
            Excludes children of the rule from the parse tree
            when set to ``True``.
        """
        self.name = name or self.__class__.__name__
        self.silent = silent
        self.silent_children = silent_children
        
    def __str__(self) -> str:
        return self.name
    
    @abstractmethod
    def grammar(self) -> Grammar:
        ...

@overload
def rule(
    fn: Callable[[], Grammar],
    /, *,
    name: None = None,
    doc: None = None,
    **kwargs: Any
) -> type[Rule]: ...

@overload
def rule(
    fn: None = None,
    /, *,
    name: Optional[str] = None,
    doc: Optional[str] = None,
    **kwargs: Any
) -> Callable[[Callable[[], Grammar]], type[Rule]]: ...

def rule(
    fn: Optional[Callable[[], Grammar]] = None,
    /, *,
    name: Optional[str] = None,
    doc: Optional[str] = None,
    **kwargs: Any
) -> Union[
    type[Rule],
    Callable[[Callable[[], Grammar]], type[Rule]],
]:
    """
    Decorator to quickly define a rule.
    
    The function that is decorated should not take any
    arguments. The function is converted into a static
    method of the newly created rule. The docstring and
    the name of the decorated function are assigned to the
    returned class.
    
    Parameters
    ----------
    fn
        The function to decorate.
    
    name
        The name of the rule. Defaults to the function's name.
    
    doc
        The docstring of the rule. Defaults to the function's docstring.
    
    kwargs
        Keyword arguments are passed into the rule's constructor.
    
    Examples
    --------
    .. code-block::
       
       from grap.core import Grammar, rule
       
        @rule
        def pet() -> Grammar:
            yield "p"
            yield "e"
            yield "t"
    
    .. code-block::
        
        from grap.core import Grammar, rule
        
        @rule(name = "dog")
        def pet() -> Grammar:
            yield "d"
            yield "o"
            yield "g"
    
    """
    def decorator(fn: Callable[[], Grammar]) -> type[Rule]:
        @define
        class R(Rule):
            def __attrs_post_init__(self) -> None:
                super().__init__(name, **kwargs)
            
            grammar: Callable[[], Grammar] = field(repr=False, default=staticmethod(fn))
        
        R.__name__ = name or fn.__name__
        R.__doc__ = doc or fn.__doc__
        return R
    
    if fn is None:
        return decorator
    return decorator(fn)


