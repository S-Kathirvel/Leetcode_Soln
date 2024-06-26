import sys
sys.set_int_max_str_digits(10000) 

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def convert(strx: str) -> int:
            num = 0
            for i in range(1, len(strx)+1):
                num += (ord(strx[-i]) - 48) * (10 ** (i-1))
            return num

        num1 = convert(num1)
        num2 = convert(num2)
        # res = '{}'.format(num1 + num2)
        # res = f'{num1 + num2}'

        return str(num1 + num2)