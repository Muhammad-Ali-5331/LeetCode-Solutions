class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        LEN = len(nums)
        nums.sort()
        def backTrack(count,li):
            if count == LEN:
                res.append(li.copy())
            else:
                i=0
                while i < LEN:
                    if nums[i] is None: 
                        i+=1
                        continue
                    li.append(nums[i])
                    nums[i] = None
                    backTrack(count+1,li)
                    nums[i] = li.pop()
                    i+=1
                    while i<LEN and nums[i-1] == nums[i]: i+=1
        backTrack(0,[])
        return res