class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) < len(nums2):
            for i in range(0, len(nums1)):
                if nums1[i] in nums2:
                    res.append(nums1[i])
                    nums2.remove(nums1[i])
                else:
                    continue
        elif len(nums2) < len(nums1):
            for i in range(0, len(nums2)):
                if nums2[i] in nums1:
                    res.append(nums2[i])
                    nums1.remove(nums2[i])
                else:
                    continue
        else:
            for i in range(0, len(nums1)):
                if nums1[i] in nums2:
                    res.append(nums1[i])
                    nums2.remove(nums1[i])
                else:
                    continue

        return res