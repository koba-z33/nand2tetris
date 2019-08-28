// set StackPointer address for test
@10
D=A
@SP
M=D

// eq 11 10 = false(0)
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

        // eq
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1
        @EQ.1
        D;JEQ
        @SP
        A=M
        M=0
        (EQ.1)
        @SP
        M=M+1

// eq 10 11 = false(0)
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

        // eq
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1
        @EQ.2
        D;JEQ
        @SP
        A=M
        M=0 
        (EQ.2)
        @SP
        M=M+1

// eq 10 10 = true(-1)
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

        // eq
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1
        @EQ.1
        D;JEQ
        @SP
        A=M
        M=0
        (EQ.1)
        @SP
        M=M+1


(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop