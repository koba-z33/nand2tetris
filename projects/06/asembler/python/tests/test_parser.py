from n2tassembler import Parser, CommandType

test_lines = (
    '// Computes R0 = 2 + 3\n',
    '\n',
    '@2\n',
    'D=A\n',
    '(LOOP)\n',
    '@3\n',
    'D=D+A\n',
    '@LOOP\n',
    '0;JMP\n',
)


def test_parser():
    parser: Parser = Parser(test_lines)

    assert parser.has_more_commands is True

    # @2
    parser.advance()
    assert parser.command.command_type == CommandType.A_COMMAND
    assert parser.command.symbol == '2'

    # D=A
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_COMMAND
    assert parser.command.dest == 'D'
    assert parser.command.comp == 'A'
    assert parser.command.jump == 'null'

    # (LOOP)
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.L_COMMAND
    assert parser.command.symbol == "LOOP"

    # @3
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.A_COMMAND
    assert parser.command.symbol == '3'

    # D=D+A
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_COMMAND
    assert parser.command.dest == 'D'
    assert parser.command.comp == 'D+A'
    assert parser.command.jump == 'null'

    # @LOOP
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.A_COMMAND
    assert parser.command.symbol == 'LOOP'

    # 0;JMP
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_COMMAND
    assert parser.command.dest == 'null'
    assert parser.command.comp == '0'
    assert parser.command.jump == 'JMP'

    assert parser.has_more_commands is False
