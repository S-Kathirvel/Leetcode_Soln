class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
# APPROACH - LISTS INITIALIZATION
	 word = list(word)
         res = []
         if ch not in word:
             return "".join(word)
         else:
             index = word.index(ch)
             for i in range(index, -1, -1):
                 res.append(word[i])
             for j in range(index+1, len(word)):
                 res.append(word[j])

             return "".join(res)

# APPROACH - STRING MANIPULATION
        if ch not in word:
            return word
        else:
            res = ""
            index = word.index(ch)
            res += word[index::-1]
            res += word[index+1::]
            return res