class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        N = len(matrix)
        res = [0]*N
        for row in matrix:
            for i in range(N): res[i]+=row[i]
        return res