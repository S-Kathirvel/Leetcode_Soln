class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        res = []
        while i < len(arr) - 2:
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                i += 1
                res.append(1)
            else:
                i += 1
                res.append(0)
        if 1 in res:
            return True
        else:
            return False