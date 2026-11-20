class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ROWS,COLS = len(matrix),len(matrix[0])
        output = []
        visited = [[False]*COLS for _ in range(ROWS)]
        def traverse(R,C,rowAdder,colAdder,out):
            APPENDED = False
            while 0<=R<ROWS and 0<=C<COLS and not visited[R][C]:
                APPENDED = True
                out.append(matrix[R][C])
                visited[R][C] = True
                R+=rowAdder
                C+=colAdder
            R-=rowAdder
            C-=colAdder
            return APPENDED,R,C

        dirs = [ [0,1], [1,0], [0,-1], [-1,0] ]
        i = 0
        sR,sC = 0,0
        while True:
            rA,cA = dirs[i]
            res,sR,sC = traverse(sR,sC,rA,cA,out=output)
            if not res: break
            i = (i+1)%4
            rA,cA = dirs[i]
            sR+= rA
            sC+= cA
        return output