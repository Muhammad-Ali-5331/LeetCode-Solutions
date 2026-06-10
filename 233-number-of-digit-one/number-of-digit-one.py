class Solution:
    def countDigitOne(self, n: int) -> int:
        def mainFunc(NUM):
            s = str(NUM)
            MAP = dict()
            def dp_func(idx,tight,lz):
                if idx == len(s): return 1,0 # Returning (no. of numbers formed, new Ones)
                key = (idx,tight,lz)
                if key in MAP: return MAP[key]
                ub = int(s[idx]) if tight else 9
                cnt,ones_cnt = 0,0
                for dig in range(ub+1):
                    new_lz = dig == 0 and lz
                    new_tight = tight and dig == ub
                    rec_res =dp_func(idx+1,new_tight,new_lz)
                    cnt+= rec_res[0]
                    ones_cnt+= rec_res[1]
                    if dig == 1: ones_cnt+= rec_res[0]
                MAP[key] = (cnt,ones_cnt)
                return MAP[key]
            return dp_func(0,True,True)[1]
        return mainFunc(n)