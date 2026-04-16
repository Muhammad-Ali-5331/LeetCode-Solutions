class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = int(dividend / divisor)
        maxr = 2**31 - 1
        belowr = -2**31
        if r>maxr:
            return maxr
        elif r<belowr:
            return belowr
        else:
            return r