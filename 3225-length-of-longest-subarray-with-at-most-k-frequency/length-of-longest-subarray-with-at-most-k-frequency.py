class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        MAP = defaultdict(int)
        mx = 1
        n = len(nums)
        nums = [0] + nums
        l,r = 1,1
        while r<=n:
            MAP[nums[r]]+=1
            while MAP[nums[r]]>k:
                MAP[nums[l]]-=1
                l+=1
            mx = max(mx,r-l+1)
            r+=1
        return mx