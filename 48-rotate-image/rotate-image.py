class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N):
            for j in range(N):
                if i == j: continue
                if i>j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in range(N):
            matrix[row] = matrix[row][::-1]