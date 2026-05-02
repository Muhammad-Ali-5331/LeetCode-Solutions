class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        LEN = len(nums)
        def subset(ind,li):
            if ind == LEN:
                res.append(li.copy())
                return 
            li.append(nums[ind])
            subset(ind+1,li)
            li.pop()
            subset(ind+1,li)
        subset(0,[])
        return res