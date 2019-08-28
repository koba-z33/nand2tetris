// set StackPointer address for test
@10
D=A
@SP
M=D

// add 7 8 = 15
    // push constant 7
    @7
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

    // add
        // pop
        @SP
        A=M-1
        D=M
        // pop
        A=A-1
        M=D+M
        // push
        D=A
        @SP
        M=D+1

// sub 5 16 = -11
    // push constant 5
    @5
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    // push constant 16
    @16
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // sub
        @SP
        A=M-1
        D=M         // pop
        A=A-1
        M=M-D       // pop
        D=A         // push
        @SP
        M=D+1

// neg 8 = -8
    // push constant 8
    @8
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // neg
        @SP
        A=M-1
        M=-M
        D=A
        @SP
        M=D+1

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
        M=-1
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
        M=-1
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
        M=-1
        @LT.3
        D;JLT
        @SP
        A=M
        M=0 
        (LT.3)
        @SP
        M=M+1

// END mark
@9999
D=A
@SP
A=M
M=D
@SP
M=M+1


(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop