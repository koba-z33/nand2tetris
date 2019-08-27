import pytest

from n2tassembler import CommandLine, Assembler


@pytest.mark.parametrize('command, machine', [
    ('@0', '0000000000000000'),
    ('@1', '0000000000000001'),
    ('D=A', '1110110000010000'),
    ('M=A', '1110110000001000'),
    ('D=D+A', '1110000010010000'),
    ('D=D+M', '1111000010010000'),
    ('0;JMP', '1110101010000111'),
    ('0;JNE', '1110101010000101'), ])
def test_assmble(command, machine):
    assembler = Assembler()

    commandline = CommandLine(0, command)
    assert assembler.make_binary(commandline) == machine


@pytest.mark.parametrize('asm_filename, hack_filename', [
    ('/home/hogege/plus.asm', '/home/hogege/plus.hack'),
    ('hogege/plus.asm', 'hogege/plus.hack'),
    ('./hogege/plus.asm', './hogege/plus.hack'),
    ('plus.asm', 'plus.hack'),
    ('C:/home/hogege/plus.asm', 'C:/home/hogege/plus.hack'),
    ('C:\\home\\hogege\\plus.asm', 'C:\\home\\hogege\\plus.hack'), ])
def test_hack_filename(asm_filename, hack_filename):
    assembler = Assembler()

    assert assembler.hack_filename(asm_filename) == hack_filename


def test_assemble_no_label():
    asm = """
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/MaxL.asm

// Symbol-less version of the Max.asm program.

@0
D=M
@1
D=D-M
@10
D;JGT
@1
D=M
@12
0;JMP
@0
D=M
@2
M=D
@14
0;JMP
"""

    asm_lines = asm.split('\n')

    hack = """0000000000000000
1111110000010000
0000000000000001
1111010011010000
0000000000001010
1110001100000001
0000000000000001
1111110000010000
0000000000001100
1110101010000111
0000000000000000
1111110000010000
0000000000000010
1110001100001000
0000000000001110
1110101010000111"""
    hack_binaries = hack.split('\n')

    assembler: Assembler = Assembler()

    binaries = assembler.assemble(asm_lines)

    assert len(binaries) == len(hack_binaries)

    for i in range(len(binaries)):
        assert binaries[i] == hack_binaries[i]


def test_assemble_label():
    asm = """
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/Max.asm

// Computes R2 = max(R0, R1)  (R0,R1,R2 refer to  RAM[0],RAM[1],RAM[2])

   @R0
   D=M              // D = first number
   @R1
   D=D-M            // D = first number - second number
   @OUTPUT_FIRST
   D;JGT            // if D>0 (first is greater) goto output_first
   @R1
   D=M              // D = second number
   @OUTPUT_D
   0;JMP            // goto output_d
(OUTPUT_FIRST)
   @R0
   D=M              // D = first number
(OUTPUT_D)
   @R2
   M=D              // M[2] = D (greatest number)
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP            // infinite loop

    """
    asm_lines = asm.split('\n')

    hack = """0000000000000000
1111110000010000
0000000000000001
1111010011010000
0000000000001010
1110001100000001
0000000000000001
1111110000010000
0000000000001100
1110101010000111
0000000000000000
1111110000010000
0000000000000010
1110001100001000
0000000000001110
1110101010000111"""
    hack_binaries = hack.split('\n')

    assembler: Assembler = Assembler()

    binaries = assembler.assemble(asm_lines)

    assert len(binaries) == len(hack_binaries)

    for i in range(len(binaries)):
        assert binaries[i] == hack_binaries[i]


def test_assemble_label():

    asm = """
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/rect/Rect.asm

// Draws a rectangle at the top-left corner of the screen.
// The rectangle is 16 pixels wide and R0 pixels high.

   @0
   D=M
   @INFINITE_LOOP
   D;JLE
   @counter
   M=D
   @SCREEN
   D=A
   @address
   M=D
(LOOP)
   @address
   A=M
   M=-1
   @address
   D=M
   @32
   D=D+A
   @address
   M=D
   @counter
   MD=M-1
   @LOOP
   D;JGT
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
   """
    asm_lines = asm.split('\n')
    hack = """0000000000000000
1111110000010000
0000000000010111
1110001100000110
0000000000010000
1110001100001000
0100000000000000
1110110000010000
0000000000010001
1110001100001000
0000000000010001
1111110000100000
1110111010001000
0000000000010001
1111110000010000
0000000000100000
1110000010010000
0000000000010001
1110001100001000
0000000000010000
1111110010011000
0000000000001010
1110001100000001
0000000000010111
1110101010000111"""

    hack_binaries = hack.split('\n')

    assembler: Assembler = Assembler()

    binaries = assembler.assemble(asm_lines)

    assert len(binaries) == len(hack_binaries)

    for i in range(len(binaries)):
        assert binaries[i] == hack_binaries[i]
