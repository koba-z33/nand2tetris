

class Code():
    """ニーモニック バイナリコード変換器 """

    def __init__(self):
        self.__dest_dic = {
            'null': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
        }

    def dest(self, mnemonic: str) -> str:
        """destバイナリ変換

        Parameters
        ----------
        mnemonic : str
            ニーモニック

        Returns
        -------
        str
            バイナリコード
        """
        return self.__dest_dic[mnemonic]
