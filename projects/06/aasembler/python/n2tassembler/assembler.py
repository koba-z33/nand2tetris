from . import CommandLine, CommandType, CommandLineError, Code


class Assembler():
    """ アセンブラ """

    def __init__(self):
        self.__code = Code()

    def make_binary(self, commandline: CommandLine) -> str:
        """コマンドから売那智コード変換
        
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
