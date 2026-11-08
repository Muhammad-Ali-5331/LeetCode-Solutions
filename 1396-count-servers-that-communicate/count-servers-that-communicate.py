from collections import defaultdict,Counter
def conert1D(r,c, totalCols):
    return r * totalCols + c

class DSU:
    def __init__(self, SIZE, R , C):
        self.parent = [i for i in range(SIZE+1)]
        self.rank = [0] * (SIZE+1)
        self.totalCols = C
        self.totalRows = R
    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def union(self, R1,C1,R2,C2):
        p1 = self.findParent(conert1D(R1,C1,self.totalCols))
        p2 = self.findParent(conert1D(R2,C2,self.totalCols))
        if p1 == p2: return
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += 1
    def attacParents(self):
        for i in range(self.totalRows):
            for j in range(self.totalCols):
                self.findParent(conert1D(i,j,self.totalCols))
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])

        d = DSU(ROWS*COLS,ROWS,COLS)
        totalComps = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:

                    totalComps+=1
                    # Left Row Check
                    for smR in range(0,col):
                        if grid[row][smR] == 1:
                            d.union(row,col,row,smR)
                    # Right Row Check
                    for lgR in range(col+1,COLS):
                        if grid[row][lgR] == 1:
                            d.union(row,col,row,lgR)
                    # Up Column Check
                    for smC in range(0,row):
                        if grid[smC][col] == 1:
                            d.union(row,col,smC,col)
                    # Down Column Check
                    for lgC in range(row+1,ROWS):
                        if grid[lgC][col] == 1:
                            d.union(row,col,lgC,col)
        d.attacParents()
        cnt = defaultdict(int)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    cnt[d.parent[conert1D(row,col, COLS)]] += 1
        return sum(v for v in cnt.values() if v > 1)