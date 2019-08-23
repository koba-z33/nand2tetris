import pytest

from n2tassembler import CommandLine, CommandType


def test_init():
    """初期化テスト
    """
    commandline = CommandLine(0, "command")
    assert commandline.line_no == 0
    assert commandline.raw_data == "command"
    assert commandline.data == "command"


def test_init_strip():
    """前後空白除去
    """
    commandline = CommandLine(1, "  command  \n")
    assert commandline.line_no == 1
    assert commandline.raw_data == "  command  \n"
    assert commandline.data == "command"


def test_init_ignorecomment():
    """コメント除去
    """
    commandline = CommandLine(123, "  command  // comment\n")
    assert commandline.line_no == 123
    assert commandline.raw_data == "  command  // comment\n"
    assert commandline.data == "command"


@pytest.mark.parametrize('raw_data, command_type',
                         [
                             ('@123', CommandType.A_COMMAND),
                             ('          @123', CommandType.A_COMMAND),
                             ('@LABEL', CommandType.A_COMMAND),
                             ('      @LABEL', CommandType.A_COMMAND),
                             ('(LABEL)', CommandType.L_COMMAND),
                             ('     (LABEL)', CommandType.L_COMMAND),
                             ('', CommandType.BLANK_LINE),
                             ('         ', CommandType.BLANK_LINE),
                             ('   // comment', CommandType.BLANK_LINE),
                             ('M=M+D', CommandType.C_COMMAND),
                         ])
def test_commandtype(raw_data, command_type):
    commandline = CommandLine(0, raw_data)
    assert commandline.command_type == command_type


def test_symbol_exception():
    commandline = CommandLine(0, "")

    with pytest.raises(CommandLineError):
        commandline.symbol()
