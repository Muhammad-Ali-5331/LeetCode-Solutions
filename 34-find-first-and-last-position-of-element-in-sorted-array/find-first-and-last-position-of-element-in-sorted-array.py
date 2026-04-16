from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def FO():
            minPos = float("inf")
            l = 0
            r = len(nums)-1
            while l<=r:
                middle = (l+r)//2
                if nums[middle] == target:
                    minPos = min(minPos,middle)
                    r = middle-1
                elif nums[middle]<target: l = middle+1
                else: r = middle-1
            return minPos
        def LO():
            l = 0
            r = len(nums)-1
            maxPos = float("-inf")
            while l<=r:
                middle = (l+r)//2
                if nums[middle] == target:
                    maxPos = max(maxPos,middle)
                    l = middle+1
                elif nums[middle]<target: l = middle+1
                else: r = middle-1
            return maxPos
        miP = FO()
        mxP = LO()
        if miP == float("inf") or mxP == float("-inf"): return [-1,-1]
        return [miP,mxP]