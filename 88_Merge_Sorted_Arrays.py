class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 +=  nums2
        nums1.sort()
        for i in range(0,n):
            if 0 in nums1:
                nums1.remove(0)
