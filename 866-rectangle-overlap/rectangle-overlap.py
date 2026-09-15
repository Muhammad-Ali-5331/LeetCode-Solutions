class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1 = rec1[0],rec1[1]
        x2,y2 = rec1[2],rec1[3]

        rec1 = [
            (x1,y2), # Upper Left-Corner
            (x1,y1), # Lower Left-Corner
            (x2,y2), # Right Upper-Corner
            (x2,y1) # Lower Right-Corner
        ]

        x1,y1 = rec2[0],rec2[1]
        x2,y2 = rec2[2],rec2[3]

        rec2 = [
            (x1,y2), # Upper Left-Corner
            (x1,y1), # Lower Left-Corner
            (x2,y2), # Right Upper-Corner
            (x2,y1) # Lower Right-Corner
        ]
        if rec2[0][0]>=rec1[2][0]: # exceeds right side
            return False
        if rec2[2][0]<=rec1[0][0]: # exceeds left side
            return False
        if rec2[1][1]>=rec1[0][1]: # exceeds upper side
            return False
        if rec2[0][1]<=rec1[1][1]: # exceeds lower side
            return False
        return True

        