from . import CommandLine, CommandType
import textwrap


class CodeWriter():
    """ コードライター """

    __seg_start = {
        'argument': 'ARG',
        'local': 'LCL',
        'static': '16',
        'this': 'THIS',
        'that': 'THAT',
    }
    __fix_seg_start = {
        'pointer': 'THIS',
        'temp': 'R5',
    }

    def makePushPopCode(self, command: CommandLine) -> str:
        if command.command_type == CommandType.C_PUSH:
            return self.__makePushCode(command)
        else:
            return self.__makePopCode(command)

    def __makePushCode(self, command: CommandLine) -> str:
        seg: str = command.arg1
        index: int = command.arg2
        if seg in self.__seg_start:
            seg_start = self.__seg_start[seg]
            return textwrap.dedent(f"""
                // push {seg} {index}
                @{index}
                D=A
                @{seg_start}
                A=M+D
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """)
        elif seg in self.__fix_seg_start:
            seg_start = self.__fix_seg_start[seg]
            return textwrap.dedent(f"""
                // push {seg} {index}
                @{index}
                D=A
                @{seg_start}
                A=A+D
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """)
        else:
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

    def __makePopCode(self, command: CommandLine) -> str:
        seg: str = command.arg1
        index: int = command.arg2
        if seg in self.__seg_start:
            seg_start = self.__seg_start[seg]
            return textwrap.dedent(f"""
                // pop {seg} {index}
                @{index}
                D=A
                @{seg_start}
                D=M+D
                @R15
                M=D
                @SP
                AM=M-1
                D=M
                @R15
                A=M
                M=D
                """)
        else:
            seg_start = self.__fix_seg_start[seg]
            return textwrap.dedent(f"""
                // pop {seg} {index}
                @{index}
                D=A
                @{seg_start}
                D=A+D
                @R15
                M=D
                @SP
                AM=M-1
                D=M
                @R15
                A=M
                M=D
                """)
