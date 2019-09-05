from n2tvmtranslator import Parser, CommandType


def test_parser():

    vmdata = """// comment
// stack operation
push constant 10
pop local 0
// arithmetic
add
sub
neg
eq
gt
lt
and
or
not
label hogege
"""
    vmdata_lines = vmdata.split('\n')

    parser = Parser(vmdata_lines)

    # push constant 0
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_PUSH
    assert parser.command.arg1 == 'constant'
    assert parser.command.arg2 == 10

    # pop local 0
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_POP
    assert parser.command.arg1 == 'local'
    assert parser.command.arg2 == 0

    # add
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'add'

    # sub
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'sub'

    # neg
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'neg'

    # eq
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'eq'

    # gt
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'gt'

    # lt
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'lt'

    # and
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'and'

    # or
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'or'

    # not
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_ARITHMETIC
    assert parser.command.arg1 == 'not'

    # label hogege
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_LABEL
    assert parser.command.arg1 == 'hogege'

    assert parser.has_more_commands is False
