class Solution:
    def maxScoreSightseeingPair(self, num: list[int]) -> int:
        mx = 0
        bst = num[0] + 0
        for i in range(1,len(num)):
            mx = max(mx,bst+num[i]-i)
            bst = max(bst,num[i]+i)
        return mx