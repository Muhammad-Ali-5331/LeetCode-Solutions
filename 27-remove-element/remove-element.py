class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        n = len(nums)
        while i<n:
            while i<n and nums[i] == val: i+=1
            if i<n:
                nums[k] = nums[i]
                k+=1
            i+=1
        return k