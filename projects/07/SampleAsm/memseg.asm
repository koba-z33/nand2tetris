// set StackPointer, Local address for test 
@20
D=A
@SP
M=D

@100
D=A
@LCL
M=D

@200
D=A
@ARG
M=D

@300
D=A
@THIS
M=D

@400
D=A
@THAT
M=D

    // push constant 1000
        // value -> D
        @1000
        D=A

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // push constant 2000
        // value -> D
        @2000
        D=A

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // push constant 3000
        // value -> D
        @3000
        D=A

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // push constant 4000
        // value -> D
        @4000
        D=A

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // pop local 0

        // calc address
        @0
        D=A
        @LCL
        D=M+D

        // address -> R15
        @R15
        M=D

        // pop -> D
        @SP
        AM=M-1
        D=M

        // D->M
        @R15
        A=M
        M=D

    // pop argument 1

        // calc address
        @1
        D=A
        @ARG
        D=M+D

        // address -> R15
        @R15
        M=D

        // pop -> D
        @SP
        AM=M-1
        D=M

        // D->M
        @R15
        A=M
        M=D

    // pop this 2

        // calc address
        @2
        D=A
        @THIS
        D=M+D

        // address -> R15
        @R15
        M=D

        // pop -> D
        @SP
        AM=M-1
        D=M

        // D->M
        @R15
        A=M
        M=D

    // pop that 3

        // calc address
        @3
        D=A
        @THAT
        D=M+D

        // address -> R15
        @R15
        M=D

        // pop -> D
        @SP
        AM=M-1
        D=M

        // D->M
        @R15
        A=M
        M=D

    // push local 1
        // calc address
        @1
        D=A
        @LCL
        A=M+D

        // M -> D
        D=M

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // push local 0
        // calc address
        @0
        D=A
        @LCL
        A=M+D

        // M -> D
        D=M

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // push local 2
        // calc address
        @2
        D=A
        @LCL
        A=M+D

        // M -> D
        D=M

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1

    // push that 3
        // calc address
        @3
        D=A
        @THAT
        A=M+D

        // M -> D
        D=M

        // push D
        @SP
        A=M
        M=D
        @SP
        M=M+1




(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop