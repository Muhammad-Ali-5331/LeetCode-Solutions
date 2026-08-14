class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mx = 0
        n = len(s)
        def check(MP):
            return all(v<=2 for v in MP.values())
        for st in range(n):
            MAP = defaultdict(int)
            for e in range(st,n):
                MAP[s[e]]+=1
                if check(MAP):
                    mx = max(mx,e-st+1)
        return mx