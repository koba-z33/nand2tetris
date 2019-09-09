from .commandtype import CommandType


class CommandLine():
    """ VMトランスレータコマンドラインオブジェクト
    """

    __type_dic = {
        '': CommandType.BLANK_LINE,
        'push': CommandType.C_PUSH,
        'pop': CommandType.C_POP,
        'label': CommandType.C_LABEL,
        'if-goto': CommandType.C_IF,
        'goto': CommandType.C_GOTO,
        'function': CommandType.C_FUNCTION,
    }

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
        self.__arg0 = self.__data.split()[0] if len(self.__data) != 0 else ''

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
        if self.__arg0 in self.__type_dic:
            return self.__type_dic[self.__arg0]
        else:
            return CommandType.C_ARITHMETIC

    @property
    def arg1(self) -> str:
        if self.command_type == CommandType.C_ARITHMETIC:
            return self.__data
        else:
            return self.__data.split()[1]

    @property
    def arg2(self) -> int:
        return int(self.__data.split()[2])
