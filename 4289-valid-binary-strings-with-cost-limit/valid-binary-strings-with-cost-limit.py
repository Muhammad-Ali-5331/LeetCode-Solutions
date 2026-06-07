class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        cost = []
        s = list("0"*n)
        def rec(idx,gC,currS):
            if idx == n:
                SUM = sum(i for i in range(n) if currS[i] == '1')
                if SUM<=k: gC.append("".join(currS))
            else:
                cS = currS[:]
                # First Choice is Keeping 1
                if idx-1>=0:
                    if cS[idx-1]!="1":
                        cS[idx] = "1"
                        rec(idx+1,gC,cS)
                else:
                    cS[idx] = "1"
                    rec(idx+1,gC,cS)
                # Second Choice Calling with 0
                cS[idx] = "0"
                rec(idx+1,gC,cS)
        rec(0,cost,s)
        return cost