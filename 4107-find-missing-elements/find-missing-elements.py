class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        curr = nums[0]
        i,n = 0,len(nums)
        while i<n:
            if curr != nums[i]:
                res.append(curr)
            else:
                i+=1
            curr+=1
        return res