class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        l = len(nums)
        al = list(set(nums))
        x = 0
        for val in nums: x^=val
        if x!=0: return l
        elif len(al) == 1 and al[0] == 0: return 0
        else: return l-1