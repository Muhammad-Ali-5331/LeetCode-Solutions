class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        inc,dec = 1,1
        ip,dp = 1,1
        for i in range(1,n):
            if nums[i]>nums[i-1]: ip+=1
            else: ip = 1
            if nums[i]<nums[i-1]: dp+=1
            else: dp = 1
            inc = max(inc,ip)
            dec = max(dec,dp)
        return max(inc,dec)