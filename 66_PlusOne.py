class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        val = 0
        for i in range(0,n):
            x = digits[i] * pow(10,n-1)
            n = n-1
            val += x
        val += 1
        res = [int(x) for x in str(val)]
        return res