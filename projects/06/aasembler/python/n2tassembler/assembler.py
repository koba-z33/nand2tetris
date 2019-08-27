import os
import sys

from . import CommandLine, CommandType, CommandLineError, Code, Parser


class Assembler():
    """ アセンブラ """

    def __init__(self):
        self.__code = Code()

    def make_binary(self, commandline: CommandLine) -> str:
        """コマンドからバイナリコード変換

        Parameters
        ----------
        commandline : CommandLine
            コマンドライン

        Returns
        -------
        str
            バイナリコード

        Raises
        ------
        CommandLineError
            ラベルコマンドを受け取ったときに発生
        """
        if commandline.command_type == CommandType.C_COMMAND:
            head = "111"
            comp = self.__code.comp(commandline.comp)
            dest = self.__code.dest(commandline.dest)
            jump = self.__code.jump(commandline.jump)
            return head + comp + dest + jump
        elif commandline.command_type == CommandType.A_COMMAND:
            return self.__code.num2bin(int(commandline.symbol))
        else:
            raise CommandLineError(str(commandline))

    def hack_filename(self, asm_filename: str) -> str:
        """hackファイル名作成

        Parameters
        ----------
        asm_filename : str
            asmファイル名

        Returns
        -------
        str
            hackファイル名
        """
        return os.path.splitext(asm_filename)[0] + '.hack'


def main():
    assembler: Assembler = Assembler()

    asm_filename: str = sys.argv[1]
    hack_filename: str = assembler.hack_filename(asm_filename)

    print('Assemble {} -> {}'.format(asm_filename, hack_filename))
