class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mi = min(nums)
        res = (mx-mi)*k
        return res