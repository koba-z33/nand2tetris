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
if-goto hoyoyo
goto hahaha
function fact 2
return
call func 2
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

    # if-goto hoyoyo
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_IF
    assert parser.command.arg1 == 'hoyoyo'

    # goto hahaha
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_GOTO
    assert parser.command.arg1 == 'hahaha'

    # function fact 2
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_FUNCTION
    assert parser.command.arg1 == 'fact'
    assert parser.command.arg2 == 2

    # return
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_RETURN

    # call func 2
    assert parser.has_more_commands is True
    parser.advance()
    assert parser.command.command_type == CommandType.C_CALL
    assert parser.command.arg1 == 'func'
    assert parser.command.arg2 == 2

    assert parser.has_more_commands is False
