import pytest

from n2tassembler import CommandLine, CommandType, CommandLineError


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


@pytest.mark.parametrize('raw_data_symbol_exception',
                         [
                             (''),              # 空行
                             ('// comment'),    # コメント行
                             ('M=M + D'),       # 演算行
                         ])
def test_symbol_exception(raw_data_symbol_exception):
    commandline = CommandLine(0, raw_data_symbol_exception)

    with pytest.raises(CommandLineError):
        commandline.symbol()


@pytest.mark.parametrize('raw_data_symbol, symbol',
                         [
                             ('@XYZ', 'XYZ'),
                             ('@1000', '1000'),
                             ('(LABEL)', 'LABEL'),
                         ]
                         )
def test_symbol(raw_data_symbol, symbol):
    commandline = CommandLine(0, raw_data_symbol)
    assert commandline.symbol == symbol


@pytest.mark.parametrize('raw_data_dest_exception',
                         [
                             (''),                  # 空行
                             ('// comment'),        # コメント行
                             ('@XYZ'),              # Aコマンド
                             ('(LABEL)'),           # ラベル
                         ]
                         )
def test_dest_exception(raw_data_dest_exception):
    commandline = CommandLine(0, raw_data_dest_exception)

    with pytest.raises(CommandLineError):
        commandline.dest()


@pytest.mark.parametrize('raw_data_dest, dest',
                         [
                             ('0:JMP', 'null'),
                             ('M=1', 'M'),
                             ('D=1', 'D'),
                             ('MD=1', 'MD'),
                             ('A=1', 'A'),
                             ('AM=1', 'AM'),
                             ('AD=1', 'AD'),
                             ('AMD=1', 'AMD'),
                         ])
def test_dest(raw_data_dest, dest):
    commandline = CommandLine(0, raw_data_dest)
    assert commandline.dest == dest


@pytest.mark.parametrize('raw_data_comp_exception',
                         [
                             (''),                  # 空行
                             ('// comment'),        # コメント行
                             ('@XYZ'),              # Aコマンド
                             ('(LABEL)'),           # ラベル
                         ]
                         )
def test_comp_exception(raw_data_comp_exception):
    commandline = CommandLine(0, raw_data_comp_exception)

    with pytest.raises(CommandLineError):
        commandline.comp()


@pytest.mark.parametrize('raw_data_comp, comp',
                         [
                             ('A=0', '0'),
                             ('A=1', '1'),
                             ('A=-1', '-1'),

                             ('A=D', 'D'),
                             ('D=A', 'A'),
                             ('D=M', 'M'),

                             ('A=!D', '!D'),
                             ('A=!A', '!A'),
                             ('D=!M', '!M'),

                             ('A=-D', '-D'),
                             ('A=-A', '-A'),
                             ('D=-M', '-M'),

                             ('A=D+1', 'D+1'),
                             ('A=A+1', 'A+1'),
                             ('D=M+1', 'M+1'),

                             ('A=D-1', 'D-1'),
                             ('A=A-1', 'A-1'),
                             ('D=M-1', 'M-1'),

                             ('A=D+A', 'D+A'),
                             ('D=D+M', 'D+M'),

                             ('A=D-A', 'D-A'),
                             ('D=D-M', 'D-M'),

                             ('A=A-D', 'A-D'),
                             ('D=M-D', 'M-D'),

                             ('A=D&A', 'D&A'),
                             ('D=D&M', 'D&M'),

                             ('A=D|A', 'D|A'),
                             ('D=D|M', 'D|M'),

                             ('0;JMP', '0'),
                             ('A;JGT', 'A'),
                             ('D;JGT', 'D'),
                         ])
def test_comp(raw_data_comp, comp):
    commandline = CommandLine(0, raw_data_comp)
    assert commandline.comp == comp


@pytest.mark.parametrize('raw_data_jump_exception',
                         [
                             (''),                  # 空行
                             ('// comment'),        # コメント行
                             ('@XYZ'),              # Aコマンド
                             ('(LABEL)'),           # ラベル
                         ]
                         )
def test_jump_exception(raw_data_jump_exception):
    commandline = CommandLine(0, raw_data_jump_exception)

    with pytest.raises(CommandLineError):
        commandline.jump()


@pytest.mark.parametrize('raw_data_jump, jump',
                         [
                             ('A=0', 'null'),
                             ('D;JGT', 'JGT'),
                             ('D;JEQ', 'JEQ'),
                             ('D;JGE', 'JGE'),
                             ('D;JLT', 'JLT'),
                             ('D;JNE', 'JNE'),
                             ('D;JLE', 'JLE'),
                             ('D;JMP', 'JMP'),
                         ])
def test_jump(raw_data_jump, jump):
    commandline = CommandLine(0, raw_data_jump)
    assert commandline.jump == jump
