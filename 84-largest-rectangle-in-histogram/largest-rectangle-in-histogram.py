class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        largestArea = 0
        stack = []
        for i in range(len(h)):
            ind = i
            while stack and stack[-1][0]>h[i]:
                he,ind = stack.pop()
                diff = i-ind
                largestArea = max(largestArea,diff*he)
            stack.append((h[i],ind))
        n = len(h)
        while stack:
            he,ind = stack.pop()
            diff = n-ind
            largestArea = max(largestArea,diff*he)
        return largestArea
            