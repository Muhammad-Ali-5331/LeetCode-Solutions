class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        dp = [[0]*cols for _ in range(rows)]
        for i in range(cols): dp[0][i] = 1
        for i in range(rows): dp[i][0] = 1
        for row in range(1,rows):
            for col in range(1,cols):
                dp[row][col] = dp[row][col-1] + dp[row-1][col]
        return dp[rows-1][cols-1]