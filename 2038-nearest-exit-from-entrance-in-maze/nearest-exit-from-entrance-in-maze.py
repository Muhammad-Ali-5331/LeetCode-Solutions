from collections import deque
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        borders = set()
        ROWS,COLS = len(maze),len(maze[0])
        def isValid(R,C): return 0<=R<ROWS and 0<=C<COLS
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(ROWS):
            if maze[r][0] != '+': borders.add((r,0))
            if maze[r][COLS-1] != '+': borders.add((r,COLS-1))
        for c in range(COLS):
            if maze[0][c]!='+': borders.add((0,c))
            if maze[ROWS-1][c]!="+": borders.add((ROWS-1,c))
        if (entrance[0],entrance[1]) in borders: borders.remove((entrance[0],entrance[1]))
        que = deque([])
        que.append((entrance[0],entrance[1],0))
        visit = set()
        while que:
            currX,currY,currD = que.popleft()
            if (currX,currY) in borders: return currD
            if (currX,currY) in visit: continue
            visit.add((currX,currY))
            for x,y in dirs:
                newX,newY = currX+x,currY+y
                if not isValid(newX,newY): continue
                if (newX,newY) in visit: continue
                if maze[newX][newY] == '+': continue
                que.append((newX,newY,currD+1))
        return -1