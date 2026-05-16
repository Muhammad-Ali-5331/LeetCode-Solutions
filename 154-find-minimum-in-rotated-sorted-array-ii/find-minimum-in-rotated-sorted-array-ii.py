from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        minE = 0
        l = 0
        r = len(nums)-1
        while l<=r:
            while l<r and nums[l] == nums[l+1]:l+=1
            while r>l and nums[r] == nums[r-1]:r-=1
            mid = (l+r)//2
            if nums[mid]<nums[minE]: minE = mid
            if nums[mid]>nums[r]: l = mid+1
            else: r = mid-1
        return nums[minE]