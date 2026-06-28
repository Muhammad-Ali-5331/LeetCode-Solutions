class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        temp=sorted(arr)
        if temp[0]!=1: temp[0] = 1
        n = len(arr)
        for i in range(1,n):
            if temp[i]-temp[i-1]<=1: continue
            else: temp[i] = temp[i-1]+1
        currMx = max(temp)
        return currMx