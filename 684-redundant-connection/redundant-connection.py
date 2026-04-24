class Union:
    def __init__(self,N):
        self.parent = {i:i for i in range(1,N+1)}
        self.rank = {i:0 for i in range(1,N+1)}

    def findP(self,node):
        if node == self.parent[node]: return node
        self.parent[node] = self.findP(self.parent[node])
        return self.parent[node]

    def union(self,node1,node2):
        p1,p2 = self.findP(node1),self.findP(node2)
        if p1 == p2: return True
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2]>self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1]+=1
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        DSU = Union(N)
        for n1,n2 in edges: 
            if DSU.union(n1,n2):
                return [n1,n2]