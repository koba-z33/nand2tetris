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
            raise CommandLineError

    @property
    def dest(self) -> str:
        """destニーモニック

        Returns
        -------
        str
            destニーモニック
        """
        if self.command_type != CommandType.C_COMMAND:
            raise CommandLineError

        pos: int = self.data.find('=')

        if pos == -1:
            return 'null'
        else:
            return self.data[0:pos]

    @property
    def comp(self) -> str:
        """compニーモニック

        Returns
        -------
        str
            compニーモニック
        """
        if self.command_type != CommandType.C_COMMAND:
            raise CommandLineError

        pos_e: int = self.data.find('=')
        pos_s: int = self.data.find(';')

        if pos_s == -1:
            return self.data[pos_e + 1:]
        else:
            return self.data[pos_e + 1:pos_s]
