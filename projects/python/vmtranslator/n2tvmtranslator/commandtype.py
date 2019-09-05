from enum import Enum


class CommandType(Enum):
    BLANK_LINE = -1
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
