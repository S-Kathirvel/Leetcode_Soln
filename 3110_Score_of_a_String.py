class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i-1]) - ord(s[i]))
        return score

        # score = 0
        # n = len(s)
        # i = 0
        # while i < n-1:
        #        score += abs(ord(s[i]) - ord(s[i+1]))
        #        i += 1
        # return score

        