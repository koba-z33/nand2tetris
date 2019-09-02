from n2tvmtranslator import CommandLine, CommandType
import pytest


def test_init():
    """初期化テスト """
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


@pytest.mark.parametrize('raw_data_command_type, command_type',
                         [
                             ('', CommandType.BLANK_LINE),
                             ('push constant 0', CommandType.C_PUSH),
                             ('pop constant 0', CommandType.C_POP),
                             ('add', CommandType.C_ARITHMETIC),
                             ('sub', CommandType.C_ARITHMETIC),
                             ('neg', CommandType.C_ARITHMETIC),
                             ('eq', CommandType.C_ARITHMETIC),
                             ('gt', CommandType.C_ARITHMETIC),
                             ('lt', CommandType.C_ARITHMETIC),
                             ('and', CommandType.C_ARITHMETIC),
                             ('or', CommandType.C_ARITHMETIC),
                             ('not', CommandType.C_ARITHMETIC),
                         ])
def test_commandtype(raw_data_command_type, command_type):
    commandline = CommandLine(0, raw_data_command_type)
    assert commandline.command_type == command_type


