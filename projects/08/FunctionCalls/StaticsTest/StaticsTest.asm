
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

// function Class1.set 0
(Class1.set)

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

// pop static 0
@SP
AM=M-1
D=M
@Class1.0
M=D

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

// pop static 1
@SP
AM=M-1
D=M
@Class1.1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

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

// function Class1.get 0
(Class1.get)

// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class1.1
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

// function Class2.set 0
(Class2.set)

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

// pop static 0
@SP
AM=M-1
D=M
@Class2.0
M=D

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

// pop static 1
@SP
AM=M-1
D=M
@Class2.1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

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

// function Class2.get 0
(Class2.get)

// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class2.1
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

// function Sys.init 0
(Sys.init)

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class1.set 2
// push return-adress
@RETURN.1
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
@Class1.set
0;JMP
// return-address
(RETURN.1)

// pop temp 0
@0
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

// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class2.set 2
// push return-adress
@RETURN.2
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
@Class2.set
0;JMP
// return-address
(RETURN.2)

// pop temp 0
@0
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

// call Class1.get 0
// push return-adress
@RETURN.3
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
@Class1.get
0;JMP
// return-address
(RETURN.3)

// call Class2.get 0
// push return-adress
@RETURN.4
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
@Class2.get
0;JMP
// return-address
(RETURN.4)

// label WHILE
(Sys.init$WHILE)

// goto WHILE
@Sys.init$WHILE
0;JMP
