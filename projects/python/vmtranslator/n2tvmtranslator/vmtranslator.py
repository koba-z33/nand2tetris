from n2tvmtranslator import CodeWriter, Parser, CommandLine
import sys
import os


class VMtranslator():

    def __init__(self):
        self.__codewriter = CodeWriter()

    def translate(self, lines: list) -> str:
        parser: Parser = Parser(lines)

        asm = ''
        while parser.has_more_commands:
            parser.advance()
            command: CommandLine = parser.command
            asm = asm + self.__codewriter.makeAssembleCode(command)

        return asm

    def asm_filename(self, vm_filename: str) -> str:
        """asmファイル名作成

        Parameters
        ----------
        vm_filename : str
            vmファイル名

        Returns
        -------
        str
            asmファイル名
        """
        return os.path.splitext(vm_filename)[0] + '.asm'


def main():
    vmtranslator = VMtranslator()

    vm_filename: str = sys.argv[1]
    asm_filename: str = vmtranslator.asm_filename(vm_filename)
    print(f'VMtranslate {vm_filename} -> {asm_filename}')

    with open(vm_filename, 'r') as f:
        vm_lines = f.readlines()

    asm = vmtranslator.translate(vm_lines)

    with open(asm_filename, 'w') as f:
        f.write(asm)
