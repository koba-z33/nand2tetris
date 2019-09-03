// set StackPointer address for test
@10
D=A
@SP
M=D

// eq 11 10 = false(0)
    @11
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // comp
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
    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    @11
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // comp
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
    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

    @10
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1

        // comp
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

(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop