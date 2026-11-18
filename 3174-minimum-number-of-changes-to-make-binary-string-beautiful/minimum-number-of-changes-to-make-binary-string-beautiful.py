class Solution:
    def minChanges(self, s: str) -> int:
        ops = 0
        n = len(s)
        for i in range(0,n-1,2):
            ops += s[i] != s[i+1]
        return ops