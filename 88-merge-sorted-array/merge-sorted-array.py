class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1.extend(nums2)
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
        """
        Do not return anything, modify nums1 in-place instead.
        """
        