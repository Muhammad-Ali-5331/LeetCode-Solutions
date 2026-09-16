class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans = 0
        MAP = dict()
        for ind,v in enumerate(nums):
            U = MAP.get(v,[0])
            U[0]+=1
            U.append(ind)
            MAP[v] = U
        for k,v in MAP.items():
            if v[0] == 3:
                ans += v[3]-v[2] == v[2]-v[1]
        return ans