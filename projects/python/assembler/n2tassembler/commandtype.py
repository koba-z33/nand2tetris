from enum import Enum


class CommandType(Enum):
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2
    BLANK_LINE = -1
