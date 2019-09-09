// set value around stackpointer

@20
M=A
@20
M=A
@21
M=A
@22
M=A
@23
M=A
@24
M=A


// set stack pointer
@20
D=A
@SP
M=D

// marking
@9999

// initialize local variable
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

