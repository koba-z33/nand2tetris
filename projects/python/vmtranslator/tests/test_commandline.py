from n2tvmtranslator import CommandLine


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
