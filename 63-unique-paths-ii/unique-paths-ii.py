class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        rows = len(Grid)
        cols = len(Grid[0])
        if Grid[0][0] == 1: return 0
        dp = [0]*cols
        dp[0] = 1
        for i in range(rows):
            for j in range(cols):
                if Grid[i][j] == 1: dp[j] = 0
                elif j > 0: dp[j]+=dp[j-1]
        return dp[cols-1]