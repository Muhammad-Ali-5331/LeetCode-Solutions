class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000: return 0
        commas = 0
        
        rem = n%1000
        q = (n // 1000)-1
        commas+=rem
        commas += q*1000 + 1
        return commas