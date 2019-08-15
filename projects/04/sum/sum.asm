// initialize loop counter
    @i
    M=1
// initialiaze sum
    @R2
    M=0
(LOOP)
// if i < 100
    @i
    D=M
    @100
    D=D-A
    @END
    D;JGT
// sum = sum + i
    @i
    D=M
    @R2
    M=D+M
// inclement counter
    @i
    M=M+1
    @LOOP
    0;JMP
(END)
    @END
    0;JMP