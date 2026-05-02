class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        LEN = len(nums)
        def subset(ind,li):
            if ind == LEN:
                res.append(li.copy())
                return 
            li.append(nums[ind])
            subset(ind+1,li)
            li.pop()
            ind+=1
            while ind < LEN and nums[ind-1] == nums[ind]: ind+=1
            subset(ind,li)
        subset(0,[])
        return res