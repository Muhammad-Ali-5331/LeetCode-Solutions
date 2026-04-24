from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = []
        adjL = defaultdict(list)
        def dfs(node, target, visit):
            if node in visit: return False
            visit.add(node)
            for ne in adjL[node]:
                if ne==target: return True
                elif ne in visit: continue
                if dfs(ne,target,visit): return True
            return False
        for x,y in edges:
            visited = set()
            if dfs(x,y,visited):
                ans = [x, y]
            adjL[x].append(y)
            adjL[y].append(x)
        return ans