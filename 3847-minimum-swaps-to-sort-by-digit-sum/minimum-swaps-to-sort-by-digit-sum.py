class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        def calD(N):
            res = 0
            while N>0:
                d = N%10
                N//=10
                res += d
            return res
        for i in range(n):
            nums[i] = (calD(nums[i]),nums[i],i)
        steps = 0
        nums.sort(key=lambda x: (x[0],x[1]))
        i = 0
        while i<n:
            if nums[i][2] == i: i+=1
            else:
                steps+=1
                nxt = nums[i][2]
                nums[i],nums[nxt] = nums[nxt],nums[i]
        return steps