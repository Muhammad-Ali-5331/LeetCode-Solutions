class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        c = 0
        n = len(nums)
        l,r = 0,1
        while r<n:
            if nums[l] == nums[r]: c +=1
            else: l=r
            r+=1

        return c