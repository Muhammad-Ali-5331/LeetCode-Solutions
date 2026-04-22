from collections import deque
from typing import List
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def isValid(r,c): return 0<=r<ROWS and 0<=c<COLS
        minTime = 0
        seen = set()
        q = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col,0))
                    seen.add((row,col))
        while q:
            currX,currY,currD = q.popleft()
            for x,y in dirs:
                newX,newY = currX+x,currY+y
                if not isValid(newX,newY): continue
                if grid[newX][newY] == 0: continue
                if (newX,newY) in seen: continue
                seen.add((newX,newY))
                minTime = max(minTime,currD+1)
                grid[newX][newY] = 2
                q.append((newX, newY, currD + 1))


        for num in grid:
            if all(True if n == 2 or n == 0 else False for n in num):continue
            else: return -1
        return minTime