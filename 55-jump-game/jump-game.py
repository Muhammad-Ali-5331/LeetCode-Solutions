class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        steps = nums[0]
        i = 0
        while steps:
            if i+1 == n: return True
            if i>n: break
            steps = max(steps-1,nums[i])
            i+=1
        return False