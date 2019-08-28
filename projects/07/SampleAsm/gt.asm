// set StackPointer address for test
@10
D=A
@SP
M=D

// gt 10 10 = false(0)
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
        @GT.1
        D;JGT
        @SP
        A=M
        M=0
        (GT.1)
        @SP
        M=M+1

// gt 10 11 = false(0)
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

        // gt
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1
        @GT.2
        D;JGT
        @SP
        A=M
        M=0 
        (GT.2)
        @SP
        M=M+1


// gt 11 10 = treu(-1)
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

        // gt
        @SP
        AM=M-1
        D=M         // pop
        @SP
        AM=M-1
        D=M-D       // pop
        M=-1
        @GT.3
        D;JGT
        @SP
        A=M
        M=0 
        (GT.3)
        @SP
        M=M+1

(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop