class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = nums[0]
        maxEnding = nums[0]
        j = 1
        for i in range(1,len(nums)):
            maxEnding = max(nums[i],maxEnding + nums[i])
            maxSum = max(maxSum,maxEnding)
        return maxSum

                