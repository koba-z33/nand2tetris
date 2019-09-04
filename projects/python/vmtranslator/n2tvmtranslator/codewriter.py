from . import CommandLine
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
