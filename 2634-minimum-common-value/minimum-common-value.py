class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set(nums2)
        for i in sorted(nums1):
            if i in seen:return i
        return -1