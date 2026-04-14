class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minDiff = float("inf")
        found = False
        d = defaultdict(list)
        for i in range(len(nums)): d[nums[i]].append(i)
        for key,value in d.items():
            if len(value) >= 3:
                found = True
                l = 0
                while l+2 < len(value):
                    i,j,k = value[l],value[l+1],value[l+2]
                    minDiff = min(minDiff,abs(i-j) + abs(j-k) + abs(k-i))
                    l+=1
        return minDiff if found else -1