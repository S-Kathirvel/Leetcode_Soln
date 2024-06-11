class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_jewels = 0
        for i in stones:
            if i in jewels:
                stone_jewels +=1
        return stone_jewels