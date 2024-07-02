class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # if len(nums1) < len(nums2):
        #     for i in range(0, len(nums1)):
        #         if nums1[i] in nums2:
        #             res.append(nums1[i])
        #             nums2.remove(nums1[i])
        #         else:
        #             continue
        # else:
        #     for i in range(0, len(nums1)):
        #         if nums1[i] in nums2:
        #             res.append(nums1[i])
        #             nums2.remove(nums1[i])
        #         else:
        #             continue

        # return list(set(res))

        set1 = set(nums1)
        set2 = set(nums2)
        output = []
        for value in set1:
            if value in set2:
                output.append(value)
        
        return output
        