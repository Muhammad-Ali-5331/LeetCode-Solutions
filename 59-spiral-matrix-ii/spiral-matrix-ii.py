class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ROWS,COLS = n,n
        output = [[0]*COLS for _ in range(ROWS)]
        visited = [[False]*COLS for _ in range(ROWS)]
        def traverse(R,C,rowAdder,colAdder,out, VAL):
            APPENDED = False
            while 0<=R<ROWS and 0<=C<COLS and not visited[R][C]:
                APPENDED = True
                out[R][C] = VAL[0]
                VAL[0]+=1
                visited[R][C] = True
                R+=rowAdder
                C+=colAdder
            R-=rowAdder
            C-=colAdder
            return APPENDED,R,C

        dirs = [ [0,1], [1,0], [0,-1], [-1,0] ]
        i = 0
        sR,sC = 0,0
        P = [1]
        while True:
            rA,cA = dirs[i]
            res,sR,sC = traverse(sR,sC,rA,cA,out=output,VAL=P)
            if not res: break
            i = (i+1)%4
            rA,cA = dirs[i]
            sR+= rA
            sC+= cA
        return output