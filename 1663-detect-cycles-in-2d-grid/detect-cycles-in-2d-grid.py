from typing import List
directions = [(-1,0),(0,1)]
class UNION:
    def __init__(self,N):
        self.parent = {i:i for i in range(N+1)}
        self.rank = {i: 0 for i in range(N + 1)}

    def findP(self,node):
        if self.parent[node] == node: return node
        self.parent[node] = self.findP(self.parent[node])
        return self.parent[node]

    def un(self,node1,node2):
        p1,p2 = self.findP(node1),self.findP(node2)
        if p1 == p2: return True
        if self.rank[p1]>=self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1]+=1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return False
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ROWS = len(grid)
        COLS = len(grid[0])
        def convert(r, c): return r*COLS + c
        def isValid(r,c): return 0<=r<ROWS and 0<=c<COLS
        DSU = UNION(ROWS*COLS)
        for row in range(ROWS):
            for col in range(COLS):
                for x,y in directions:
                    newX,newY = row+x,col+y
                    if not isValid(newX,newY): continue
                    if grid[newX][newY] == grid[row][col]:
                        if DSU.un(convert(row,col),convert(newX,newY)): return True
        return False