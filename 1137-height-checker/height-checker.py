class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        t = sorted(heights)
        n = len(heights)
        return sum(1 if heights[i]!=t[i] else 0 for i in range(n))