from .commandtype import CommandType


class CommandLine():
    """ VMトランスレータコマンドラインオブジェクト
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
        self.__data = self.__raw_data.split('//', 1)[0].strip()

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
        """行データ

        Returns
        -------
        str
            行データ
        """
        return self.__data

    @property
    def command_type(self) -> CommandType:
        if len(self.__data) == 0:
            return CommandType.BLANK_LINE
        elif self.__data.startswith('push'):
            return CommandType.C_PUSH
        elif self.__data.startswith('pop'):
            return CommandType.C_POP
        else:
            return CommandType.C_ARITHMETIC

    @property
    def arg1(self) -> str:
        if self.command_type == CommandType.C_ARITHMETIC:
            return self.__data
        elif self.command_type == CommandType.C_POP:
            return self.__data.split()[1]
        elif self.command_type == CommandType.C_PUSH:
            return self.__data.split()[1]

    @property
    def arg2(self) -> int:
        if self.command_type == CommandType.C_POP:
            return int(self.__data.split()[2])
        elif self.command_type == CommandType.C_PUSH:
            return int(self.__data.split()[2])
