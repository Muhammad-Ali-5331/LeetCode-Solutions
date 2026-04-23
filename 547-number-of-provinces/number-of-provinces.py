class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(1,n+1)}
        self.rank = {i:0 for i in range(1,n+1)}
        self.prov = n

    def findParent(self,node):
        if node == self.parent[node]: return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self,node1,node2):
        p1,p2 = self.findParent(node1),self.findParent(node2)
        if p1 == p2: return
        if self.rank[p1]>self.rank[p2]: self.parent[p2] = p1
        elif self.rank[p2]>self.rank[p1]: self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1]+=1
        self.prov-=1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        DSU = UnionFind(N)
        for i in range(N):
            for j in range(N):
                if isConnected[i][j] == 0: continue
                DSU.union(i+1,j+1)
        # -- It is Done for Path Compression of rem elements -- #
        #for i in range(N): DSU.findParent(i+1) , if this is done then return len(set(DSU.parent.values()))
        return DSU.prov