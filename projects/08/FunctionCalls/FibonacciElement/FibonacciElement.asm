
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

// function Main.fibonacci 0
(Main.fibonacci)

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

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
M=-1
@COMP.0
D;JLT
@SP
A=M
M=0
(COMP.0)
@SP
M=M+1

// if-goto IF_TRUE
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE

// goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP

// label IF_TRUE
(Main.fibonacci$IF_TRUE)

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

// label IF_FALSE
(Main.fibonacci$IF_FALSE)

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

// push constant 2
@2
D=A
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

// call Main.fibonacci 1
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
@1
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
@Main.fibonacci
0;JMP
// return-address
(RETURN.1)

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

// push constant 1
@1
D=A
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

// call Main.fibonacci 1
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
@1
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
@Main.fibonacci
0;JMP
// return-address
(RETURN.2)

// add
@SP
A=M-1
D=M
A=A-1
M=M+D
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

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.fibonacci 1
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
@1
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
@Main.fibonacci
0;JMP
// return-address
(RETURN.3)

// label WHILE
(Sys.init$WHILE)

// goto WHILE
@Sys.init$WHILE
0;JMP
