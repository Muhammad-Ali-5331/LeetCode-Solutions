class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MAP = defaultdict(list)
        for x,y in edges: MAP[x].append(y)
        mxD = [0]
        def dfs(node,mD,SEEN):
            SEEN[node] = True
            if not node in MAP: return 0
            d = 0
            for child in MAP[node]:
                d = max(d,dfs(child,mD,SEEN))
            d+=1
            mD[0] = max(mD[0],d)
            return d
        seen = [False]*(len(edges)+5)
        for x,y in edges:
            if seen[x]: continue
            dfs(x,mxD,seen)
        MOD = 10**9 + 7
        return pow(2,mxD[0]-1) % MOD