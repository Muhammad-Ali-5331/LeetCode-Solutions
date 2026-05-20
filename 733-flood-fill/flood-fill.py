from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS,COLS = len(image),len(image[0])
        def isValid(r,c): return 0<=r<ROWS and 0<=c<COLS
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        q = deque()
        if image[sr][sc]!=color:
            q.append((sr,sc))
            start = image[sr][sc]
            while q:
                curX,curY = q.pop()
                image[curX][curY] = color
                for x,y in dirs:
                    nX,nY = x+curX,y+curY
                    if not isValid(nX,nY): continue
                    if image[nX][nY] == start: q.append((nX,nY))
        return image
