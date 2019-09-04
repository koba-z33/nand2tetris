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
