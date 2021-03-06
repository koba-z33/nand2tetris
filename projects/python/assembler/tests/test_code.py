import pytest

from n2tassembler import Code


@pytest.mark.parametrize('mnemonic_dest, binary_dest',
                         [
                             ('null', '000'),
                             ('M', '001'),
                             ('D', '010'),
                             ('MD', '011'),
                             ('A', '100'),
                             ('AM', '101'),
                             ('AD', '110'),
                             ('AMD', '111'),
                         ])
def test_dest(mnemonic_dest, binary_dest):
    code = Code()

    assert code.dest(mnemonic_dest) == binary_dest


@pytest.mark.parametrize('mnemonic_comp, binary_comp',
                         [
                             ('0', '0101010'),
                             ('1', '0111111'),
                             ('-1', '0111010'),

                             ('D', '0001100'),
                             ('A', '0110000'),
                             ('M', '1110000'),

                             ('!D', '0001101'),
                             ('!A', '0110001'),
                             ('!M', '1110001'),

                             ('-D', '0001111'),
                             ('-A', '0110011'),
                             ('-M', '1110011'),

                             ('D+1', '0011111'),
                             ('A+1', '0110111'),
                             ('M+1', '1110111'),

                             ('D-1', '0001110'),
                             ('A-1', '0110010'),
                             ('M-1', '1110010'),

                             ('D+A', '0000010'),
                             ('D+M', '1000010'),

                             ('D-A', '0010011'),
                             ('D-M', '1010011'),

                             ('A-D', '0000111'),
                             ('M-D', '1000111'),

                             ('D&A', '0000000'),
                             ('D&M', '1000000'),

                             ('D|A', '0010101'),
                             ('D|M', '1010101'),
                         ])
def test_comp(mnemonic_comp, binary_comp):
    code = Code()

    assert code.comp(mnemonic_comp) == binary_comp


@pytest.mark.parametrize('mnemoni_jump, binary_jump',
                         [
                             ('null', '000'),
                             ('JGT', '001'),
                             ('JEQ', '010'),
                             ('JGE', '011'),
                             ('JLT', '100'),
                             ('JNE', '101'),
                             ('JLE', '110'),
                             ('JMP', '111'),
                         ])
def test_jump(mnemoni_jump, binary_jump):
    code = Code()

    assert code.jump(mnemoni_jump) == binary_jump


@pytest.mark.parametrize('num2bin_data, binary_num',
                         [
                             (0, '0000000000000000'),
                             (1, '0000000000000001'),
                             (100, '0000000001100100'),
                             (32767, '0111111111111111'),
                             (21845, '0101010101010101'),
                         ])
def test_num2bin(num2bin_data, binary_num):
    code = Code()

    assert code.num2bin(num2bin_data) == binary_num
