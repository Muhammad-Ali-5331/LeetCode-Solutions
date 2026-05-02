class Solution:
    def climbStairs(self, n: int) -> int:
        MAP = {1:1,2:2}
        def climb(n):
            if n in MAP: return MAP[n] 
            MAP[n] = climb(n-1) + climb(n-2)
            return MAP[n]
        return climb(n)