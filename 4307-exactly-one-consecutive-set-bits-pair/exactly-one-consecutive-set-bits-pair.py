class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        prev = 0
        for i in range(32):
            mask = 1<<i
            if n&mask and prev: count+=1
            prev = n&mask
        return count==1