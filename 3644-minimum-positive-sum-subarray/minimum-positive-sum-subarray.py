class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mi = float('inf')
        n = len(nums)
        for i in range(n):
            cs = 0
            for j in range(i,n):
                cs+=nums[j]
                if l<=j-i+1<=r:
                    if cs > 0: mi = min(mi,cs)
                elif j-i+1>r: break
        return -1 if mi == float("inf") else mi