class Solution:
    def romanToInt(self, s: str) -> int:
        val = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        summ = 0
        i = 0

        while i < len(s):
            if i < len(s)-1 and val[s[i]] < val[s[i+1]]:
                summ += val[s[i+1]] - val[s[i]]
                i = i + 2
            else:
                summ += val[s[i]]
                i += 1
        return summ
