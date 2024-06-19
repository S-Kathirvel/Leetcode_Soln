class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = list(s.split(' '))
        res = ""
        for i in range(0, len(str_list)):
            if str_list[i].isalnum():
                res = res + str_list[i]
            else:
                string = str_list[i]
                res += ''.join(l for l in string if l.isalnum())
             
        if res.lower() == res[::-1].lower():
            return True
        else:
            return False