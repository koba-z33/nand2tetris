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
