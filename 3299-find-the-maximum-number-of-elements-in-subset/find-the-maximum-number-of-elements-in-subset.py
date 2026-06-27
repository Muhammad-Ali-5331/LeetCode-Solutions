class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        MAP = defaultdict(int)
        for num in nums: MAP[num]+=1
        res = 1
        if 1 in MAP: res = max(res,MAP[1]-1 if MAP[1]%2 == 0 else MAP[1])
        for num in MAP:
            if num==1: continue
            subs = []
            t = num
            while t in MAP:
                subs.append(t)
                t*=t
            if MAP[subs[0]]<=1: continue
            count = 0
            for NUM in subs:
                if MAP[NUM]>=2:
                    count+=1
                else: break
            if count == len(subs): count-=1
            res = max(res,count*2 + 1)
        return res