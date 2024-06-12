class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [v for v in nums if v != val]
        k = len(nums)
        return k