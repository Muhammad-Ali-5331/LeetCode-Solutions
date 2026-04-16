class Solution:
    def combinationSum(self,nums: List[int], target: int) -> List[List[int]]:
        res = []
        LEN = len(nums)
        def func(ind,t,li):
            if t<0: return
            elif t==0:  res.append(li.copy())
            elif ind==LEN: return
            else:
                li.append(nums[ind])
                func(ind,t-nums[ind],li)
                li.pop()
                func(ind+1,t,li)
        func(0,target,[])
        return res