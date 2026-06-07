class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        s = 0
        for i in range(1000):
            s+= i if (abs(n-i)<=k) and (n&i == 0) else 0
        return s