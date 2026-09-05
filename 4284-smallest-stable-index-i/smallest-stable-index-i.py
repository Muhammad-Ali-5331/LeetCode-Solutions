class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mxR,miR = [-1]*n,[-1]*n
        mxR[0],miR[n-1] = nums[0],nums[n-1]
        for i in range(1,n): mxR[i] = max(mxR[i-1],nums[i])
        for i in range(n-2,-1,-1): miR[i] = min(miR[i+1],nums[i])
        for i in range(n):
            res = mxR[i] - miR[i]
            if res <= k:
                return i
        return -1