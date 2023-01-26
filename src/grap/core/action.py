from enum import auto, IntEnum

class Action(IntEnum):
    GO_BACK = auto()
    NO_MATCH = auto()
    IS_MATCH = auto()
    OPTIONAL = auto()
    REQUIRE = auto()

