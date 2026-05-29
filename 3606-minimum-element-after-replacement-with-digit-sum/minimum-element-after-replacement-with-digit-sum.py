class Solution:
    def minElement(self, nums: List[int]) -> int:
        minE = float("inf")
        for num in nums: 
            minE = min(minE,sum(map(int,list(str(num)))))
        return minE