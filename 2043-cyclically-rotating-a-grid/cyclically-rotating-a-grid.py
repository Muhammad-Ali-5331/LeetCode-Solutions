from collections import deque
from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        startR,startC,endR,endC = 0,0,ROWS-1,COLS-1
        while startR<endR and startC<endC:
            tempArr = deque([])
            for r in range(startR,endR+1): tempArr.append(grid[r][startC])
            for c in range(startC+1,endC+1): tempArr.append(grid[endR][c])
            for r in range(endR-1,startR-1,-1): tempArr.append(grid[r][endC])
            for c in range(endC-1,startC,-1): tempArr.append(grid[startR][c])
            #print(tempArr)
            tempK = k%len(tempArr)
            tempArr.rotate(tempK)
            #print(tempArr)
            i = 0
            for r in range(startR,endR+1): grid[r][startC] = tempArr[i];i+=1
            for c in range(startC+1,endC+1): grid[endR][c] = tempArr[i];i+=1
            for r in range(endR-1,startR-1,-1): grid[r][endC] = tempArr[i];i+=1
            for c in range(endC-1,startC,-1): grid[startR][c] = tempArr[i];i+=1
            startR, startC, endR, endC = startR+1,startC+1,endR-1,endC-1
        return grid