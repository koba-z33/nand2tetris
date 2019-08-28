// set StackPointer address for test
@10
D=A
@SP
M=D

// lt 10 10 = false(0)
    // push constant 10
    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    // push constant 10
    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // lt
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1        // set true
        @LT.1
        D;JLT
        @SP
        A=M
        M=0
        (LT.1)
        @SP
        M=M+1

// lt 11 10 = false(0)
    // push constant 11
    @11
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    // push constant 10
    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // lt
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1        // set true
        @LT.2
        D;JLT
        @SP
        A=M
        M=0 
        (LT.2)
        @SP
        M=M+1


// lt 10 11 = treu(-1)
    // push constant 10
    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    // push constant 11
    @11
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // lt
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1        // set true
        @LT.3
        D;JLT
        @SP
        A=M
        M=0         // set false 
        (LT.3)
        @SP
        M=M+1

(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop