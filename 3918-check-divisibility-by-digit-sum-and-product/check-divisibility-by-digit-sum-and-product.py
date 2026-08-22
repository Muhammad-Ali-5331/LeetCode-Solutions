class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s,p = 0,1
        tempN = n
        while tempN>0:
            lastD = tempN%10
            s+=lastD
            p*=lastD
            tempN//=10
        return n % (s+p) == 0