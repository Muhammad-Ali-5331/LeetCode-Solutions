class Solution:
    def countDaysTogether(self, aA: str, aL: str, bA: str, bL: str) -> int:
        res = [0]*366
        md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alAM,alAD = map(int,aA.split("-"))
        sA = (sum(md[:alAM]))+alAD
        alDM,alDD = map(int,aL.split("-"))
        eA = (sum(md[:alDM]))+alDD
        for i in range(sA,eA+1): res[i]+=1
        
        bAM,blAD = map(int,bA.split("-"))
        sB = sum(md[:bAM]) + blAD
        blDM,blDD = map(int,bL.split("-"))
        eB = sum(md[:blDM]) + blDD
        
        for i in range(sB,eB+1): res[i]+=1
        return res.count(2)