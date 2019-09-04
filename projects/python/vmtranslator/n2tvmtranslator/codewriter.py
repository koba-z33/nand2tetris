from . import CommandLine, CommandType
import textwrap


class CodeWriter():
    """ コードライター """

    __seg_start = {
        'argument': ('ARG', 'M'),
        'local': ('LCL', 'M'),
        'static': ('16', 'M'),
        'this': ('THIS', 'M'),
        'that': ('THAT', 'M'),
        'pointer': ('THIS', 'A'),
        'temp': ('R5', 'A'),
    }
    __operator_2_variable = {
        'add': 'M+D',
        'sub': 'M-D',
        'and': 'M&D',
        'or': 'M|D',
    }
    __operator_1_variable = {
        'neg': '-M',
        'not': '!M',
    }
    __operator_comp = {
        'eq': 'JEQ',
        'gt': 'JGT',
        'lt': 'JLT',
    }

    def __init__(self):
        self.__comp_index = 0

    def makeAssembleCode(self, command: CommandLine) -> str:
        if command.command_type == CommandType.C_POP:
            return self.__makePopCode(command)
        elif command.command_type == CommandType.C_PUSH:
            return self.__makePushCode(command)
        elif command.command_type == CommandType.C_ARITHMETIC:
            return self.__makeArithmetic(command)

    def __makePushCode(self, command: CommandLine) -> str:
        seg: str = command.arg1
        index: int = command.arg2
        if seg == 'constant':
            return textwrap.dedent(f"""
                // push {seg} {index}
                @{index}
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """)
        else:
            seg_start = self.__seg_start[seg]
            return textwrap.dedent(f"""
                // push {seg} {index}
                @{index}
                D=A
                @{seg_start[0]}
                A={seg_start[1]}+D
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """)

    def __makePopCode(self, command: CommandLine) -> str:
        seg: str = command.arg1
        index: int = command.arg2
        seg_start = self.__seg_start[seg]
        return textwrap.dedent(f"""
            // pop {seg} {index}
            @{index}
            D=A
            @{seg_start[0]}
            D={seg_start[1]}+D
            @R15
            M=D
            @SP
            AM=M-1
            D=M
            @R15
            A=M
            M=D
            """)

    def __makeArithmetic(self, command: CommandLine) -> str:
        operator_name: str = command.arg1

        if operator_name in self.__operator_2_variable:
            operator: str = self.__operator_2_variable[operator_name]
            return textwrap.dedent(f"""
                // {operator_name}
                @SP
                A=M-1
                D=M
                A=A-1
                M={operator}
                D=A
                @SP
                M=D+1
                """)
        elif operator_name in self.__operator_1_variable:
            operator: str = self.__operator_1_variable[operator_name]
            return textwrap.dedent(f"""
                // {operator_name}
                @SP
                AD=M-1
                M={operator}
                @SP
                M=D+1
                """)
        else:
            jump_label = f'COMP.{self.__comp_index}'
            self.__comp_index = self.__comp_index + 1
            operator: str = self.__operator_comp[operator_name]
            return textwrap.dedent(f"""
                // {operator_name}
                @SP
                AM=M-1
                D=M
                @SP
                AM=M-1
                D=M-D
                M=-1
                @{jump_label}
                D;{operator}
                @SP
                A=M
                M=0
                ({jump_label})
                @SP
                M=M+1
                """)
