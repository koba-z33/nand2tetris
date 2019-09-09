
// function SimpleFunction.test 2
(SimpleFunction.SimpleFunction.test)

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

// push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@1
D=A
@LCL
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

// not
@SP
AD=M-1
M=!M
@SP
M=D+1

// push argument 0
@0
D=A
@ARG
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

// push argument 1
@1
D=A
@ARG
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
