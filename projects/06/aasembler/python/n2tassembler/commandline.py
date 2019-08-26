from .commandtype import CommandType
from .commandlineerror import CommandLineError


class CommandLine():
    """アセンブラコマンドラインオブジェクト

    """

    def __init__(self, line_no: int, raw_data: str):
        """コンストラクタ

        Parameters
        ----------
        line_no : int
            行番号
        raw_data : str
            行生データ
        """
        self.__line_no = line_no
        self.__raw_data = raw_data
        self.__data = self.raw_data.split('//', 1)[0].strip()

    @property
    def line_no(self) -> int:
        """行番号

        Returns
        -------
        int
            行番号
        """
        return self.__line_no

    @property
    def raw_data(self) -> str:
        """行生データ

        Returns
        -------
        str
            行生データ
        """
        return self.__raw_data

    @property
    def data(self) -> str:
        """コマンドデータ

        Returns
        -------
        str
            コマンドデータ
        """

        return self.raw_data.split('//', 1)[0].strip()

    @property
    def command_type(self) -> CommandType:
        """コマンドタイプ

        Returns
        -------
        CommandType
            コマンドタイプ
        """
        if len(self.__data) == 0:
            return CommandType.BLANK_LINE
        if self.__data[0] == '@':
            return CommandType.A_COMMAND
        elif self.__data[0] == '(':
            return CommandType.L_COMMAND
        else:
            return CommandType.C_COMMAND

    @property
    def symbol(self) -> str:
        """シンボル

        Returns
        -------
        str
            シンボル

        Raises
        ------
        CommandLineError
            A命令、ラベル以外のコマンドの時に発生
        """
        if self.command_type == CommandType.A_COMMAND:
            return self.data[1:]
        elif self.command_type == CommandType.L_COMMAND:
            return self.data[1:-1]
        else:
            raise CommandLineError(str(self))

    @property
    def dest(self) -> str:
        """destニーモニック

        Returns
        -------
        str
            destニーモニック
        """
        return self.__sepalate_mnemonic()[0]

    @property
    def comp(self) -> str:
        """compニーモニック

        Returns
        -------
        str
            compニーモニック
        """
        return self.__sepalate_mnemonic()[1]

    @property
    def jump(self) -> str:
        """jumpニーモニック

        Returns
        -------
        str
            jumpニーモニック
        """
        return self.__sepalate_mnemonic()[2]

    def __sepalate_mnemonic(self) -> tuple:
        """ニーモニック分割

        Returns
        -------
        tuple
            分割されたニーモニック
        """
        if self.command_type != CommandType.C_COMMAND:
            raise CommandLineError(str(self))

        pos_e: int = self.data.find('=')
        pos_s: int = self.data.find(';')

        if pos_e == -1:
            dest = 'null'
        else:
            dest = self.data[0:pos_e]

        if pos_s == -1:
            comp = self.data[pos_e + 1:]
        else:
            comp = self.data[pos_e + 1:pos_s]

        if pos_s == -1:
            jump = 'null'
        else:
            jump = self.data[pos_s + 1:]

        return (dest, comp, jump)

    def __str__(self):
        return 'LineNo {} : {}'.format(self.line_no, self.__raw_data)
