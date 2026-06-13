from functools import lru_cache
class Solution:
    @classmethod
    def countDistinct(self, n: int) -> int:
        def mainFunc(NUM):
            s = str(NUM)
            L = len(s)
            @lru_cache(None)
            def dp_func(idx,tight,lz):
                if idx == L: return not lz
                upperBound = int(s[idx]) if tight else 9
                res = 0
                for dig in range(upperBound+1):
                    if not lz and dig == 0: continue
                    new_lz = lz and (dig == 0)
                    new_tight = tight and (dig == upperBound)
                    res+= dp_func(idx+1,new_tight,new_lz)
                return res
            return dp_func(0,True,True)
        return mainFunc(n)
# n = int(input())
# print(Solution.countDistinct(n))