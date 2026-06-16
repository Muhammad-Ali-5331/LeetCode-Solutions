class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        n = len(nums)
        while i<n:
            nums[k] = nums[i]
            while i<n and nums[i] == nums[k]: i+=1
            k+=1
        return k