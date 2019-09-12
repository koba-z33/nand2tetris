from n2tvmtranslator import CodeWriter, Parser, CommandLine
import sys
import os


class VMtranslator():

    def __init__(self):
        self.__codewriter = CodeWriter()
        self.is_make_init = True

    def translate(self, filename: str) -> str:
        with open(filename, 'r') as f:
            vm_lines = f.readlines()

        parser: Parser = Parser(vm_lines)

        self.__codewriter.vm_filename = self.__strip_vm_filename(filename)

        if self.is_make_init is True:
            asm = self.__codewriter.makeInit()
        else:
            asm = ''
        self.is_make_init = False

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
        if os.path.isfile(abs_path):
            asm_file = os.path.splitext(abs_path)[0] + '.asm'
            vm_files = [abs_path]
        else:
            asm_file = os.path.join(abs_path,
                                    os.path.basename(abs_path) + '.asm')
            vm_files = glob.glob(os.path.join(abs_path, '*.vm'))

        return {
            'asm_file': asm_file,
            'vm_files': vm_files,
        }

    @staticmethod
    def __strip_vm_filename(vm_filename: str) -> str:
        return os.path.splitext(os.path.basename(vm_filename))[0]


def main():
    argv: str = sys.argv[1]

    vmtranslator = VMtranslator()

    file_info = vmtranslator.make_file_info(argv)

    if len(sys.argv) > 2 and sys.argv[2] == '--noInit':
        vmtranslator.is_make_init = False

    print(f'VMtranslate {argv} -> {file_info["asm_file"]}')

    asm = ''
    for vm_file in file_info['vm_files']:
        print(f'translate {vm_file}')
        asm = asm + vmtranslator.translate(vm_file)

    with open(file_info['asm_file'], 'w') as f:
        f.write(asm)
