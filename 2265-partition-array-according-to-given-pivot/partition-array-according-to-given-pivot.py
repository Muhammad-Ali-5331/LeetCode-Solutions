class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        g = []
        e = []
        i = 0
        while i<len(nums):
            if nums[i]<pivot:l.append(nums[i])
            elif nums[i]>pivot: g.append(nums[i])
            else: e.append(nums[i])
            i+=1
        return l+e+g