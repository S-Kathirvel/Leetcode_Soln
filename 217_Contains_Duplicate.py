class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = list(set(nums))
        x.sort()
        nums.sort()
        if x == nums:
            return False
        else:
            return True