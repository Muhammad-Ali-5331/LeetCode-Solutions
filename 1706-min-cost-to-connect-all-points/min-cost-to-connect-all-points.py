from collections import defaultdict
from typing import List
from heapq import heappop,heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        cost = 0
        adj = defaultdict(list)
        for i in range(N):
            currX,currY = points[i]
            for j in range(i+1,N):
                nextX,nextY = points[j]
                dist = abs(currX-nextX)+abs(currY-nextY)
                adj[(currX,currY)].append([nextX,nextY,dist])
                adj[(nextX,nextY)].append([currX,currY,dist])
        minHeap = []
        p1 = tuple(points.pop(0))
        visit = defaultdict(bool)
        visit[p1] = True
        for neX,neY,d in adj[p1]: heappush(minHeap,(d,neX,neY))
        while minHeap:
            currCost,curX,curY = heappop(minHeap)
            if visit[(curX,curY)]: continue
            visit[(curX,curY)] = True
            cost+=currCost
            for neighX,neighY,DIST in adj[(curX,curY)]:
                if not visit[(neighX,neighY)]: heappush(minHeap,(DIST,neighX,neighY))
        return cost