class Solution:
    def maxArea(self, height: List[int]) -> int:
        lower = 0
        higher = len(height) - 1
        maxArea = 0
        while lower < higher:
            currentArea = (higher-lower) * min(height[lower],height[higher])
            maxArea = max(maxArea,currentArea)
            if height[lower] < height[higher]:
                lower+=1
            else:
                higher-=1
        return maxArea