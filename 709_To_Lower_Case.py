class Solution:
    def toLowerCase(self, s: str) -> str:
        st = ""
        for i in range(0,len(s)):
            upp_ascii = ord(s[i])
            if  upp_ascii > 64 and upp_ascii < 91:
                low_ascii = chr(upp_ascii+32)
                st += low_ascii
            else: 
                st += s[i]
        return st