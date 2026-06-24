class Solution:
    def maxDistance(self, moves: str) -> int:
        x,y = 0,0
        MOVS = {"U": [0,-1],"D": [0,1], "L":[-1,0],"R": [1,0]}
        C = Counter(moves)
        if '_' in C: del C["_"]
        if C:
            mx = max(C,key = C.get)
        else: return moves.count('_')
        for ch in moves:
            if ch in MOVS:
                xM,yM = MOVS[ch]
                x+=xM
                y+=yM
            else:
                xM,yM = MOVS[mx]
                x+=xM
                y+=yM

        return abs(x)+abs(y)