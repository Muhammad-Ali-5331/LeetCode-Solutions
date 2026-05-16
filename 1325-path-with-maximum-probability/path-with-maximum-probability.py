import heapq
from collections import defaultdict
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        res = 0.0
        adj = defaultdict(list)
        for ind in range(len(edges)):
            u = edges[ind][0]
            v = edges[ind][1]
            adj[u].append((succProb[ind],v))
            adj[v].append((succProb[ind],u))
        q = []
        distances = [0.0]*(n+1)
        heapq.heappush(q,(-1,start_node))
        visit = set()
        while q:
            currD,currN = heapq.heappop(q)
            currD*=-1
            if currN in visit: continue
            visit.add(currN)
            for d,neigh in adj[currN]:
                newDist = currD*d
                if distances[neigh]<=newDist:
                    distances[neigh] = newDist
                    heapq.heappush(q,(-newDist,neigh))

        return distances[end_node]