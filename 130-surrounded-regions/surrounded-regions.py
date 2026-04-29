from typing import List
class Solution:
    def __init__(self):
        self.ROWS = 0
        self.COLS = 0
        self.directions = []
    def isValid(self, r, c): return 0 <= r < self.ROWS and 0 <= c < self.COLS
    def solve(self, board: List[List[str]]) -> None:
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.ROWS = len(board)
        self.COLS = len(board[0])
        def dfs(R,C):
            if not self.isValid(R,C): return
            if board[R][C] in {'T','X'}: return
            board[R][C] = 'T'
            for x,y in self.directions:
                dfs(R+x,C+y)
        for i in range(self.ROWS):
            if board[i][0] == 'O': dfs(i,0)
            if board[i][self.COLS-1] == 'O': dfs(i,self.COLS-1)
        for i in range(self.COLS):
            if board[0][i] == 'O': dfs(0,i)
            if board[self.ROWS-1][i] == 'O':dfs(self.ROWS-1,i)
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == 'O': board[row][col] = 'X'
                if board[row][col] == 'T': board[row][col] = 'O'