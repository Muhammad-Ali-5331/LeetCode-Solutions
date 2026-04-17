class Solution:
    def trap(self, height: List[int]) -> int:
        leftP = 0
        rightP = len(height) - 1
        ans = 0
        lmax = float("-inf")
        rmax = float("-inf")
        while leftP < rightP:
            lmax = max(lmax,height[leftP])
            rmax = max(rmax,height[rightP])
            if lmax < rmax:
                ans+=lmax-height[leftP]
                leftP+=1
            else:
                ans+=rmax-height[rightP]
                rightP-=1
        return ans