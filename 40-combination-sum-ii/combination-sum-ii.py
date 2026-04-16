class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        LEN = len(nums)
        nums.sort()
        def func(ind,t,li):
            if t<0:return
            elif t==0: res.append(li[::1])
            elif ind==LEN: return
            else:
                li.append(nums[ind])
                func(ind+1,t-nums[ind],li)
                li.pop()
                i = ind+1
                while ind+1 < LEN and nums[ind] == nums[ind+1]: ind+=1
                func(ind+1,t,li)
        func(0,target,[])
        return res