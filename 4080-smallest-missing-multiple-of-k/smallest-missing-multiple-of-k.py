class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        vals = set(nums)
        mult = k
        while mult in vals:
            mult+=k
        return mult