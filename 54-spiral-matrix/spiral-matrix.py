from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowLeftToRight = 0
        bottomRow = ROWS-1
        endCol = COLS-1
        currCol = 0
        while rowLeftToRight<bottomRow and currCol<endCol:
        # -- Traversing Top Most Row (left --> right while leaving last val) -- #
            colPointer = currCol
            while colPointer<=endCol:
                res.append(matrix[rowLeftToRight][colPointer])
                colPointer+=1
        # -- Traversing Right Most Col (up -- > down while leaving last val) -- #
            rowPointer = rowLeftToRight+1
            while rowPointer<=bottomRow:
                res.append(matrix[rowPointer][endCol])
                rowPointer+=1
        # -- Traversing Bottom Most Row (right --> left while leaving the left most val) -- #
            colPointer = endCol-1
            while colPointer>=currCol:
                res.append(matrix[bottomRow][colPointer])
                colPointer-=1
        # -- Traversing Left Most Col (down --> up)
            rowPointer = bottomRow-1
            while rowPointer>rowLeftToRight:
                res.append(matrix[rowPointer][currCol])
                rowPointer-=1

            # -- Incrementing/Decrementing Pointers -- #
            rowLeftToRight+=1
            bottomRow-=1
            currCol+=1
            endCol-=1
        if rowLeftToRight == bottomRow:
            while currCol<=endCol:
                res.append(matrix[rowLeftToRight][currCol])
                currCol+=1
        if currCol == endCol:
            while rowLeftToRight<=bottomRow:
                res.append(matrix[rowLeftToRight][currCol])
                rowLeftToRight+=1
        return res