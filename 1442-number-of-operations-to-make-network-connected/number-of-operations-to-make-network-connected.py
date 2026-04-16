class Union:
    def __init__(self,N):
        self.parent = {i:i for i in range(N+1)}
        self.rank = {i:0 for i in range(N+1)}


    def findP(self,node):
        if self.parent[node] == node: return node
        self.parent[node] = self.findP(self.parent[node])
        return self.parent[node]


    def union(self,node1,node2):
        p1,p2 = self.findP(node1),self.findP(node2)
        if p1 == p2: return 1
        if self.rank[p1]>=self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1]+=1
        else:
            self.parent[p1] = p2
            self.rank[p2]+=1
        return 0
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        N = len(connections)
        extraCables = 0
        DSU = Union(n)
        for n1,n2 in connections: extraCables += DSU.union(n1,n2)
        comps = n-(N-extraCables)
        if extraCables>= comps-1: return comps-1
        else: return -1