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
        @SP
        A=M-1
        D=M
        A=A-1
        M=M+D
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
        D=M
        A=A-1
        M=M-D
        D=A
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.1
        D;JEQ
        @SP
        A=M
        M=0
        (COMP.1)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.2
        D;JEQ
        @SP
        A=M
        M=0 
        (COMP.2)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.3
        D;JEQ
        @SP
        A=M
        M=0
        (COMP.3)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.4
        D;JGT
        @SP
        A=M
        M=0
        (COMP.4)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.5
        D;JGT
        @SP
        A=M
        M=0 
        (COMP.5)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.6
        D;JGT
        @SP
        A=M
        M=0 
        (COMP.6)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.7
        D;JLT
        @SP
        A=M
        M=0
        (COMP.7)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.8
        D;JLT
        @SP
        A=M
        M=0 
        (COMP.8)
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
        D=M
        @SP
        AM=M-1
        D=M-D
        M=-1
        @COMP.9
        D;JLT
        @SP
        A=M
        M=0 
        (COMP.9)
        @SP
        M=M+1

// and 127 170 = 42
    // push constant 127
    @127
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    // push constant 170
    @170
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
        M=M&D
        D=A
        @SP
        M=D+1

// or 5 16 = 21
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
        D=M
        A=A-1
        M=M|D
        D=A
        @SP
        M=D+1

// not 21845 = -21846
    // push constant 0
    @21845
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // not
        @SP
        A=M-1
        M=!M
        D=A
        @SP
        M=D+1



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