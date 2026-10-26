class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        R = len(grid)
        C = len(grid[0])
        def dfs(x,y):
            res = 0
            res += grid[x][y] % k
            grid[x][y] = 0
            for X,Y in dirs:
                nX,nY = x+X, y+Y
                if nX<0 or nX>=R or nY<0 or nY>=C: continue
                if grid[nX][nY] == 0: continue
                res += (dfs(nX,nY) % k)
            return res

        Res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]!=0:
                    loc = dfs(r,c)
                    Res += (loc%k == 0)
        return Res