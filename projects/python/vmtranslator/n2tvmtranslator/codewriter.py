from . import CommandLine, CommandType
import textwrap


class LabelIncrementer():

    def __init__(self, name: str):
        self.__name = name
        self.__index = 0

    def name(self) -> str:
        label = f'{self.__name}.{self.__index}'
        self.__index = self.__index + 1
        return label


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

    __tmp_pop = 'R15'
    __tmp_frame = 'R14'
    __tmp_ret = 'R13'

    def __init__(self):
        self.vm_filename = ''
        self._vm_funcname = ''
        self.__comp_label = LabelIncrementer('COMP')
        self.__return_label = LabelIncrementer('RETURN')

    @property
    def vm_filename(self) -> str:
        return self.__vm_filename

    @vm_filename.setter
    def vm_filename(self, v: str):
        self.__vm_filename = v

    @property
    def _vm_funcname(self) -> str:
        return self.__vm_funcname

    @_vm_funcname.setter
    def _vm_funcname(self, v: str):
        self.__vm_funcname = v

    def makeInit(self) -> str:
        call_init = self.__makeCall(CommandLine(-1, 'call Sys.init 0'))

        return textwrap.dedent(f"""
            // bootstrap
            @256    // set stack-pointer
            D=A
            @SP
            M=D
            """) + call_init

    def makeAssembleCode(self, command: CommandLine) -> str:
        if command.command_type == CommandType.C_POP:
            return self.__makePopCode(command)
        elif command.command_type == CommandType.C_PUSH:
            return self.__makePushCode(command)
        elif command.command_type == CommandType.C_ARITHMETIC:
            return self.__makeArithmetic(command)
        elif command.command_type == CommandType.C_LABEL:
            return self.__makeLabel(command)
        elif command.command_type == CommandType.C_IF:
            return self.__makeIfGoto(command)
        elif command.command_type == CommandType.C_GOTO:
            return self.__makeGoto(command)
        elif command.command_type == CommandType.C_FUNCTION:
            return self.__makeFunction(command)
        elif command.command_type == CommandType.C_RETURN:
            return self.__makeReturn(command)
        elif command.command_type == CommandType.C_CALL:
            return self.__makeCall(command)
        else:
            raise Exception('Unknown command')

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
        elif seg == 'static':
            return textwrap.dedent(f"""
                // push {seg} {index}
                @{self.__vm_filename}.{index}
                D=M
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
        if seg == 'static':
            return textwrap.dedent(f"""
                // pop {seg} {index}
                @SP
                AM=M-1
                D=M
                @{self.__vm_filename}.{index}
                M=D
                """)
        else:
            return textwrap.dedent(f"""
                // pop {seg} {index}
                @{index}
                D=A
                @{seg_start[0]}
                D={seg_start[1]}+D
                @{self.__tmp_pop}
                M=D
                @SP
                AM=M-1
                D=M
                @{self.__tmp_pop}
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
            jump_label = self.__comp_label.name()

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

    def __makeLabel(self, command: CommandLine) -> str:
        return textwrap.dedent(f"""
                // label {command.arg1}
                ({self.__makeLabelStr(command.arg1)})
                """)

    def __makeIfGoto(self, command: CommandType) -> str:
        return textwrap.dedent(f"""
                // if-goto {command.arg1}
                @SP
                AM=M-1
                D=M
                @{self.__makeLabelStr(command.arg1)}
                D;JNE
                """)

    def __makeGoto(self, command: CommandLine) -> str:
        return textwrap.dedent(f"""
                // goto {command.arg1}
                @{self.__makeLabelStr(command.arg1)}
                0;JMP
                """)

    def __makeLabelStr(self, label: str) -> str:
        return f'{self._vm_funcname}${label}'

    def __makeFunction(self, command: CommandLine) -> str:
        self._vm_funcname = command.arg1
        asm = textwrap.dedent(f"""
                // function {command.arg1} {command.arg2}
                ({command.arg1})
                """)
        for i in range(command.arg2):
            asm = asm + textwrap.dedent("""
                        @SP
                        A=M
                        M=0
                        @SP
                        M=M+1
                        """)
        return asm

    def __makeReturn(self, command: CommandLine) -> str:
        return textwrap.dedent(f"""
                // return
                @LCL    // FRAME = LCL
                D=M
                @{self.__tmp_frame}
                M=D
                @5      // RET = *(FRAME-5)
                D=A
                @{self.__tmp_frame}
                A=M-D
                D=M
                @{self.__tmp_ret}
                M=D
                @SP     // *ARG = pop()
                AM=M-1
                D=M
                @ARG
                A=M
                M=D
                @ARG    // SP = ARG+1
                D=M+1
                @SP
                M=D
                @1      // THAT = *(FRAME-1)
                D=A
                @{self.__tmp_frame}
                A=M-D
                D=M
                @THAT
                M=D
                @2      // THIS = *(FRAME-2)
                D=A
                @{self.__tmp_frame}
                A=M-D
                D=M
                @THIS
                M=D
                @3      // ARG = *(FRAME-3)
                D=A
                @{self.__tmp_frame}
                A=M-D
                D=M
                @ARG
                M=D
                @4      // LCL = *(FRAME-4)
                D=A
                @{self.__tmp_frame}
                A=M-D
                D=M
                @LCL
                M=D
                @{self.__tmp_ret}    // goto RET
                A=M
                0;JMP
                """)

    def __makeCall(self, command: CommandLine) -> str:
        return_label = self.__return_label.name()

        return textwrap.dedent(f"""
                // call {command.arg1} {command.arg2}
                // push return-adress
                @{return_label}
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1
                @LCL    // push LCL
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                @ARG    // push ARG
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                @THIS   // push THIS
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                @THAT   // push THAT
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                @SP     // ARG = SP-n-5
                D=M
                @{command.arg2}
                D=D-A
                @5
                D=D-A
                @ARG
                M=D
                @SP     // LCL = SP
                D=M
                @LCL
                M=D
                // goto f
                @{command.arg1}
                0;JMP
                // return-address
                ({return_label})
                """)
