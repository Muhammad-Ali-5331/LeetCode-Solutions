class Solution:
    def __init__(self):
        self.orgBorad = None
        self.res = 0
        self.COLS = None
        self.ROWS = None

    def notAttacked(self,row,col,Board):
        #Check If there is no queen in current column where we want to place this queen
        #Running a column Based Loop
        for COL in range(row): 
            if Board[COL][col] == 'Q': return False
        
        #Check if not attacked from left upper diagnal
        decreasingRow = row-1
        decreasingCol = col-1
        while decreasingRow >= 0 and decreasingCol >= 0:
            if Board[decreasingRow][decreasingCol] == 'Q': return False
            decreasingRow-=1
            decreasingCol-=1
        
        #Check if not attacked from right upper diagnal
        decreasingRow = row-1
        increasingCol = col+1
        while decreasingRow >= 0 and increasingCol < self.COLS:
            if Board[decreasingRow][increasingCol] == 'Q': return False
            decreasingRow-=1
            increasingCol+=1

        return True #If not attacked from left upper diagonal, right upper diagonal, and current col then queen can be placed here


    def CheckNextRow(self,row,currBoard):

        if row == self.ROWS:
            self.res+=1
            return

        for col in range(self.ROWS):
            if (self.notAttacked(row,col,currBoard)):
                currBoard[row][col] = 'Q'
                self.CheckNextRow(row+1,currBoard)
                currBoard[row][col] = '.'
    def totalNQueens(self, n: int) -> int:
        self.ROWS = self.COLS = n
        self.board = [["." for _ in range(n)] for _ in range(n)]
        currBoard = self.board[::]
        self.CheckNextRow(0,currBoard)
        return self.res