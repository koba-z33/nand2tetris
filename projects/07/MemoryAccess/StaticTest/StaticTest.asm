
// push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop static 8
@8
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

// pop static 1
@1
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

// push static 3
@3
D=A
@16
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@1
D=A
@16
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A
@SP
M=D+1

// push static 8
@8
D=A
@16
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
A=M-1
D=M
A=A-1
M=M+D
D=A
@SP
M=D+1
