from contextlib import suppress
from itertools import count
from . import rule

class Identifier(rule.Rule):
    def expect(self):
        yield rule.Validate(
            lambda char: char.isalnum() or char in "-_",
            name = "alphanumeric / '-' / '_'"
        )

class RuleDeclaration(rule.Rule):
    def expect(self):
        yield rule.String("[")
        yield Identifier
        yield rule.String("]")

class RuleContent(rule.Rule):
    def expect(self):
        with supress(ParseError):
            while True: yield ???
        yield Action.GO_BACK

class Rule(rule.Rule):
    def expect(self):
        yield RuleDeclaration
        yield rule.String("\n")
        yield RuleContent

class Statement(rule.Rule):
    def expect(self):
        yield rule.String("load", ignore_case = True)
        yield Whitespace
        yield rule.String("*") | rule.Identifier
        yield Whitespace
        yield rule.String("from", ignore_case = True)
        yield Whitespace
        yield rule.Identifier

class Document(rule.Rule):
    def expect(self):
        with supress(ParseError):
            while True: yield Statement | Rule
        yield rule.EOF

