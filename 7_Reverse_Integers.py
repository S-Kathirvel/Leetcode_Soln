class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            int_str = str(x)
            rev_str = int_str[::-1]
            rev_int = int(rev_str)
            if rev_int.bit_length() >= 32 :
                rev_int = 0
                return rev_int
            else:
                return rev_int
        elif x==0:
            return 0
        else:
            x = -x
            return -(self.reverse(x))