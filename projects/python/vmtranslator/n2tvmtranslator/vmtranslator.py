from n2tvmtranslator import CodeWriter, Parser, CommandLine
import sys
import os


class VMtranslator():

    def __init__(self):
        self.__codewriter = CodeWriter()

    def translate(self, filename: str) -> str:
        with open(filename, 'r') as f:
            vm_lines = f.readlines()

        parser: Parser = Parser(vm_lines)

        asm = ''
        while parser.has_more_commands:
            parser.advance()
            command: CommandLine = parser.command
            asm = asm + self.__codewriter.makeAssembleCode(command)

        return asm

    def make_file_info(self, argv: str) -> dict:
        """VMtranslatorの入出力ファイル情報の作成

        Parameters
        ----------
        argv : str
            コマンドライン引数

        Returns
        -------
        dict
            入出力情報dict
        """
        import glob

        abs_path = os.path.abspath(argv)
        asm_file = os.path.splitext(abs_path)[0] + '.asm'
        if os.path.isfile(abs_path):
            vm_files = [abs_path]
        else:
            vm_files = glob.glob(os.path.join(abs_path, '*.vm'))

        return {
            'asm_file': asm_file,
            'vm_files': vm_files,
        }


def main():
    argv: str = sys.argv[1]

    vmtranslator = VMtranslator()

    file_info = vmtranslator.make_file_info(argv)

    print(f'VMtranslate {argv} -> {file_info["asm_file"]}')

    asm = ''
    for vm_file in file_info['vm_files']:
        print(f'translate {vm_file}')
        asm = asm + vmtranslator.translate(vm_file)

    with open(file_info['asm_file'], 'w') as f:
        f.write(asm)
