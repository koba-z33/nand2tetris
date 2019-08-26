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
