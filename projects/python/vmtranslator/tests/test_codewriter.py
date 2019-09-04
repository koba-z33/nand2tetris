from n2tvmtranslator import CodeWriter, CommandLine


def test_push_argument():
    command = CommandLine(0, 'push argument 3')
    codewriter = CodeWriter()
    expected = """
// push argument 3
@3
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_argument():
    command = CommandLine(0, 'pop argument 3')
    codewriter = CodeWriter()
    expected = """
// pop argument 3
@3
D=A
@ARG
D=M+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_local():
    command = CommandLine(0, 'push local 10')
    codewriter = CodeWriter()
    expected = """
// push local 10
@10
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_local():
    command = CommandLine(0, 'pop local 3')
    codewriter = CodeWriter()
    expected = """
// pop local 3
@3
D=A
@LCL
D=M+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_static():
    command = CommandLine(0, 'push static 100')
    codewriter = CodeWriter()
    expected = """
// push static 100
@100
D=A
@16
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_static():
    command = CommandLine(0, 'pop static 3')
    codewriter = CodeWriter()
    expected = """
// pop static 3
@3
D=A
@16
D=M+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_constant():
    command = CommandLine(0, 'push constant 10')
    codewriter = CodeWriter()
    expected = """
// push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_this():
    command = CommandLine(0, 'push this 5')
    codewriter = CodeWriter()
    expected = """
// push this 5
@5
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_this():
    command = CommandLine(0, 'pop this 3')
    codewriter = CodeWriter()
    expected = """
// pop this 3
@3
D=A
@THIS
D=M+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_that():
    command = CommandLine(0, 'push that 5')
    codewriter = CodeWriter()
    expected = """
// push that 5
@5
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_that():
    command = CommandLine(0, 'pop that 3')
    codewriter = CodeWriter()
    expected = """
// pop that 3
@3
D=A
@THAT
D=M+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_pointer():
    command = CommandLine(0, 'push pointer 0')
    codewriter = CodeWriter()
    expected = """
// push pointer 0
@0
D=A
@THIS
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_pointer():
    command = CommandLine(0, 'pop pointer 1')
    codewriter = CodeWriter()
    expected = """
// pop pointer 1
@1
D=A
@THIS
D=A+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_push_temp():
    command = CommandLine(0, 'push temp 3')
    codewriter = CodeWriter()
    expected = """
// push temp 3
@3
D=A
@R5
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makePushPopCode(command) == expected


def test_pop_temp():
    command = CommandLine(0, 'pop temp 6')
    codewriter = CodeWriter()
    expected = """
// pop temp 6
@6
D=A
@R5
D=A+D
@R15
M=D
@SP
AM=M-1
D=M
@R15
A=M
M=D
"""

    assert codewriter.makePushPopCode(command) == expected


def test_add():
    command = CommandLine(0, 'add')
    codewriter = CodeWriter()
    expected = """
// add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A
@SP
M=D+1
"""

    assert codewriter.makeArithmetic(command) == expected


def test_sub():
    command = CommandLine(0, 'sub')
    codewriter = CodeWriter()
    expected = """
// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A
@SP
M=D+1
"""

    assert codewriter.makeArithmetic(command) == expected


def test_neg():
    command = CommandLine(0, 'neg')
    codewriter = CodeWriter()
    expected = """
// neg
@SP
AD=M-1
M=-M
@SP
M=D+1
"""

    assert codewriter.makeArithmetic(command) == expected


def test_eq_gt_lt():
    """
    add test jump label increment.
    """
    codewriter = CodeWriter()

    command_eq = CommandLine(0, 'eq')
    expected_eq = """
// eq
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMP.0
D;JEQ
@SP
A=M
M=0
(COMP.0)
@SP
M=M+1
"""

    command_gt = CommandLine(1, 'gt')
    expected_gt = """
// gt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMP.1
D;JGT
@SP
A=M
M=0
(COMP.1)
@SP
M=M+1
"""

    command_lt = CommandLine(2, 'lt')
    expected_lt = """
// lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMP.2
D;JLT
@SP
A=M
M=0
(COMP.2)
@SP
M=M+1
"""

    assert codewriter.makeArithmetic(command_eq) == expected_eq
    assert codewriter.makeArithmetic(command_gt) == expected_gt
    assert codewriter.makeArithmetic(command_lt) == expected_lt


def test_and():
    command = CommandLine(0, 'and')
    codewriter = CodeWriter()
    expected = """
// and
@SP
A=M-1
D=M
A=A-1
M=M&D
D=A
@SP
M=D+1
"""

    assert codewriter.makeArithmetic(command) == expected


def test_or():
    command = CommandLine(0, 'or')
    codewriter = CodeWriter()
    expected = """
// or
@SP
A=M-1
D=M
A=A-1
M=M|D
D=A
@SP
M=D+1
"""

    assert codewriter.makeArithmetic(command) == expected


def test_not():
    command = CommandLine(0, 'not')
    codewriter = CodeWriter()
    expected = """
// not
@SP
AD=M-1
M=!M
@SP
M=D+1
"""

    assert codewriter.makeArithmetic(command) == expected
