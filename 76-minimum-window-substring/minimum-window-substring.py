class Solution:
    def minWindow(self, t: str, f: str) -> str:
        MAPF = Counter(f)
        MAPT = defaultdict(int)
        need = sum(MAPF.values())
        having = 0
        minL = float("inf")
        l = 0
        r = 0
        minl = 0
        while r < len(t):
            if t[r] in MAPF:
                MAPT[t[r]]+=1
                if MAPT[t[r]] <= MAPF[t[r]]:
                    having+=1
                if having == need:
                    if r-l+1 < minL:
                        minL = r-l+1
                        minl = l
                    while l <= r and having == need:
                        if t[l] in MAPF:
                            if MAPT[t[l]] > MAPF[t[l]]:
                                    MAPT[t[l]]-=1
                            else:
                                if r-l+1 < minL:
                                    minL = r-l+1
                                    minl = l
                                MAPT[t[l]]-=1
                                having-=1
                        l+=1
            r+=1
        if minL == float("inf"):
            return ""  # No valid window exists
        return t[minl:minl+minL]