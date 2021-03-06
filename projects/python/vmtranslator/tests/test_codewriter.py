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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


def test_push_static():
    command = CommandLine(0, 'push static 100')
    codewriter = CodeWriter()
    codewriter.vm_filename = 'vm_name'
    expected = """
// push static 100
@vm_name.100
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

    assert codewriter.makeAssembleCode(command) == expected


def test_pop_static():
    command = CommandLine(0, 'pop static 3')
    codewriter = CodeWriter()
    codewriter.vm_filename = 'vm_name'
    expected = """
// pop static 3
@SP
AM=M-1
D=M
@vm_name.3
M=D
"""

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    codewriter.vm_filename = "test"
    assert codewriter.makeAssembleCode(command_eq) == expected_eq
    assert codewriter.makeAssembleCode(command_gt) == expected_gt
    codewriter.vm_filename = "test2"
    assert codewriter.makeAssembleCode(command_lt) == expected_lt


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


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

    assert codewriter.makeAssembleCode(command) == expected


def test_label():
    command_func = CommandLine(0, 'function func1 2')
    command = CommandLine(1, 'label hogege')
    command_return = CommandLine(2, 'return')

    codewriter = CodeWriter()
    expected_in_func = """
// label hogege
(func1$hogege)
"""
    expected_out_func = """
// label hogege
($hogege)
"""

    # out function
    assert codewriter.makeAssembleCode(command) == expected_out_func
    # in function
    codewriter.makeAssembleCode(command_func)
    assert codewriter.makeAssembleCode(command) == expected_in_func
    codewriter.makeAssembleCode(command_return)
    # out function
    assert codewriter.makeAssembleCode(command) == expected_in_func


def test_if_goto():
    command_func = CommandLine(0, 'function func3 2')
    command = CommandLine(1, 'if-goto hoyoyo')
    command_return = CommandLine(2, 'return')

    codewriter = CodeWriter()
    codewriter.vm_filename = 'test'
    expected_in_func = """
// if-goto hoyoyo
@SP
AM=M-1
D=M
@func3$hoyoyo
D;JNE
"""

    expected_out_func = """
// if-goto hoyoyo
@SP
AM=M-1
D=M
@$hoyoyo
D;JNE
"""

    # out function
    assert codewriter.makeAssembleCode(command) == expected_out_func
    # in function
    codewriter.makeAssembleCode(command_func)
    assert codewriter.makeAssembleCode(command) == expected_in_func
    codewriter.makeAssembleCode(command_return)
    # out function
    assert codewriter.makeAssembleCode(command) == expected_in_func


def test_goto():
    command_func = CommandLine(0, 'function func 2')
    command = CommandLine(1, 'goto hahaha')
    command_return = CommandLine(2, 'return')

    codewriter = CodeWriter()
    codewriter.vm_filename = 'test'
    expected_in_func = """
// goto hahaha
@func$hahaha
0;JMP
"""

    expected_out_func = """
// goto hahaha
@$hahaha
0;JMP
"""

    # out function
    assert codewriter.makeAssembleCode(command) == expected_out_func
    # in function
    codewriter.makeAssembleCode(command_func)
    assert codewriter.makeAssembleCode(command) == expected_in_func
    codewriter.makeAssembleCode(command_return)
    # out function
    assert codewriter.makeAssembleCode(command) == expected_in_func


def test_function():
    command = CommandLine(0, 'function fact 3')
    codewriter = CodeWriter()
    codewriter.vm_filename = 'test'
    expected = """
// function fact 3
(fact)

@SP
A=M
M=0
@SP
M=M+1

@SP
A=M
M=0
@SP
M=M+1

@SP
A=M
M=0
@SP
M=M+1
"""

    assert codewriter.makeAssembleCode(command) == expected


def test_return():
    command = CommandLine(0, 'return')
    codewriter = CodeWriter()
    codewriter.vm_filename = 'test'
    expected = """
// return
@LCL    // FRAME = LCL
D=M
@R14
M=D
@5      // RET = *(FRAME-5)
D=A
@R14
A=M-D
D=M
@R13
M=D
@SP     // *ARG = pop()
AM=M-1
D=M
@ARG
A=M
M=D
@ARG    // SP = ARG+1
D=M+1
@SP
M=D
@1      // THAT = *(FRAME-1)
D=A
@R14
A=M-D
D=M
@THAT
M=D
@2      // THIS = *(FRAME-2)
D=A
@R14
A=M-D
D=M
@THIS
M=D
@3      // ARG = *(FRAME-3)
D=A
@R14
A=M-D
D=M
@ARG
M=D
@4      // LCL = *(FRAME-4)
D=A
@R14
A=M-D
D=M
@LCL
M=D
@R13    // goto RET
A=M
0;JMP
"""

    assert codewriter.makeAssembleCode(command) == expected


def test_call():
    command = CommandLine(0, 'call func 2')
    codewriter = CodeWriter()
    expected = """
// call func 2
// push return-adress
@RETURN.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL    // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG    // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS   // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT   // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP     // ARG = SP-n-5
D=M
@2
D=D-A
@5
D=D-A
@ARG
M=D
@SP     // LCL = SP
D=M
@LCL
M=D
// goto f
@func
0;JMP
// return-address
(RETURN.0)
"""

    assert codewriter.makeAssembleCode(command) == expected


def test_makeInit():
    codewriter = CodeWriter()
    expected = """
// bootstrap
@256    // set stack-pointer
D=A
@SP
M=D

// call Sys.init 0
// push return-adress
@RETURN.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL    // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG    // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS   // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT   // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP     // ARG = SP-n-5
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP     // LCL = SP
D=M
@LCL
M=D
// goto f
@Sys.init
0;JMP
// return-address
(RETURN.0)
"""

    assert codewriter.makeInit() == expected
