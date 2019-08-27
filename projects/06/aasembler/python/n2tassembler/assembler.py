import os
import sys

from . import CommandLine, CommandType, CommandLineError, Code, Parser


class Assembler():
    """ アセンブラ """

    def __init__(self):
        self.__code = Code()
        self.__symbol = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576,
        }
        self.__next_value_address = 16

    def assemble(self, asm_lines: list) -> list:
        """アセンブル

        Parameters
        ----------
        lines : list
            アセンブラコードリスト

        Returns
        -------
        list
            バイナリコードリスト
        """
        parser: Parser = Parser(asm_lines)

        rom_address: int = 0

        while parser.has_more_commands:
            parser.advance()
            command: CommandLine = parser.command
            if command.command_type == CommandType.L_COMMAND:
                self.__symbol[command.symbol] = rom_address
            else:
                rom_address = rom_address + 1

        parser.reset()

        binaries: list = []
        while parser.has_more_commands:
            parser.advance()
            command: CommandLine = parser.command
            if command.command_type != CommandType.L_COMMAND:
                binaries.append(self.make_binary(command))

        return binaries

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
            return self.__get_acommand_value(commandline.symbol)
        else:
            raise CommandLineError(str(commandline))

    def __get_acommand_value(self, label: str) -> str:
        """Aコマンドのバイナリコード取得

        Parameters
        ----------
        label : str
            Aコマンドシンボル

        Returns
        -------
        str
            Aコマンドバイナリコード
        """
        value = label

        # 数値でなければ、シンボルテーブルから値を探す。
        # シンボルテーブルに、存在しない場合、
        # 新しい変数アドレスを取得して、シンボルテーブルに追加
        if label.isdigit() is False:
            if value not in self.__symbol:
                self.__symbol[value] = self.__next_value_address
                self.__next_value_address = self.__next_value_address + 1
            value = self.__symbol[value]

        return self.__code.num2bin(int(value))

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

    with open(asm_filename, 'r') as f:
        asm_lines = f.readlines()

    binaries: list = assembler.assemble(asm_lines)

    with open(hack_filename, 'w') as f:
        f.writelines('\n'.join(binaries))
