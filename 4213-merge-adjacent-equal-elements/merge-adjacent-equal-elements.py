class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            currNum = num
            while stack and stack[-1] == currNum:
                stack.pop()
                currNum+=currNum
            stack.append(currNum)
        return stack