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
        self.reset()

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
    def command(self) -> CommandLine:
        """現コマンド

        Returns
        -------
        str
            コマンド
        """
        return self.__lines[self.__memory_pos]

    def reset(self):
        """カウンタリセット
        """
        self.__memory_pos = -1
