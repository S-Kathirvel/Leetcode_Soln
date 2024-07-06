class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1
        k = 1
        for i in range(time):
            if k==1 or k==n:
                direction *= -1
                k += direction
            else:
                k += direction
        return k