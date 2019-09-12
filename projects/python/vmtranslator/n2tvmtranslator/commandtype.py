from enum import Enum


class CommandType(Enum):
    BLANK_LINE = -1
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_IF = 4
    C_GOTO = 5
    C_FUNCTION = 6
    C_RETURN = 7
    C_CALL = 8
