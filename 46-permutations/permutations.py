class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        LEN = len(nums)
        def backTrack(li,count):
            if count == LEN:
                res.append(li.copy())
                return
            for i in range(LEN):
                if nums[i] is None: continue
                li.append(nums[i])
                nums[i] = None
                backTrack(li,count+1)
                nums[i] = li.pop()
        backTrack([],0)
        return res