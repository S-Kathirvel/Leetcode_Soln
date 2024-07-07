class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        direction = -1
        z = 0
        for i in range(k):
            if z==0 or z==n-1:
                direction *= -1
                z += direction
            else:
                z += direction
        return z