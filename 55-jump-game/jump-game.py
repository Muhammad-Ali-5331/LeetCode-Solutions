class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        dp = [0]*n
        dp[0] = nums[0]
        i = 0
        while True:
            if i+1 == n: return True
            if i>n: break
            dp[i] = max(dp[i-1 if i-1>=0 else 0]-1,nums[i])
            if dp[i] == 0: break
            i+=1
        return False