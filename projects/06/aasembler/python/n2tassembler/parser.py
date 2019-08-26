from . import CommandLine, CommandType


class Parser():
    """パーサー """

    def __init__(self, lines: list):
        """コンストラクタ

        Parameters
        ----------
        lines : list
            読み込み行
        """
        self.__lines = []
        for lineno, line in enumerate(lines):
            commandline = CommandLine(lineno, line)
            if commandline.command_type != CommandType.BLANK_LINE:
                self.__lines.append(commandline)
        self.__memory_pos = -1

    @property
    def has_more_commands(self) -> bool:
        """次のコマンドがあるかどうか

        Returns
        -------
        bool
            True：存在する
        """
        return len(self.__lines) > self.__memory_pos + 1

    def advance(self) -> None:
        """次のコマンドを読み込み現コマンドとする。 """
        self.__memory_pos = self.__memory_pos + 1

    @property
    def command_type(self) -> CommandType:
        """現コマンドのコマンドタイプ

        Returns
        -------
        str
            コマンドタイプ
        """
        return self.__lines[self.__memory_pos].command_type

    @property
    def symbol(self) -> str:
        """現コマンドのシンボルを返す

        Returns
        -------
        str
            シンボル
        """
        return self.__lines[self.__memory_pos].symbol

    @property
    def dest(self) -> str:
        """destニーモニック

        Returns
        -------
        str
            destニーモニック
        """
        return self.__lines[self.__memory_pos].dest

    @property
    def comp(self) -> str:
        """compニーモニック

        Returns
        -------
        str
            compニーモニック
        """
        return self.__lines[self.__memory_pos].comp

    @property
    def jump(self) -> str:
        """jumpニーモニック

        Returns
        -------
        str
            jumpニーモニック
        """
        return self.__lines[self.__memory_pos].jump
