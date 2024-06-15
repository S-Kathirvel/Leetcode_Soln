class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         n  = dict()
#         for i in range(0, len(nums)):
#             n[nums.count(nums[i])] = nums[i]
#         return n.get(1)