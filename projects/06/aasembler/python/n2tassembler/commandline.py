from .commandtype import CommandType


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
