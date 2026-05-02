class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startrow = 0
        endrow = len(matrix)-1
        while startrow <= endrow:
            middlerow = (startrow+endrow)//2
            if matrix[middlerow][0] <= target <= matrix[middlerow][-1]:
                start = 0
                end = len(matrix[middlerow]) - 1
                while start <= end:
                    middleindex = (start+end) // 2
                    if matrix[middlerow][middleindex] == target:
                        return True
                    elif target > matrix[middlerow][middleindex]:
                        start = middleindex + 1
                    else:
                        end = middleindex - 1
                return False
            elif target > matrix[middlerow][0]:
                startrow = middlerow + 1
            else:
                endrow = middlerow-1
        return False