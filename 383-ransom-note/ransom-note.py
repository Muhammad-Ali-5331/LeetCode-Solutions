class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        d = Counter(m)
        for k,v in Counter(r).items():
            if k not in d: return False
            elif v>d[k]: return False
        return True