class Solution:
    def secondsBetweenTimes(self, sT: str, eT: str) -> int:
        hr,mi,ss = int(sT[0]+sT[1]),int(sT[3]+sT[4]),int(sT[6]+sT[7])
        res1 = (hr*3600) + (mi*60) + ss
        hr,mi,ss = int(eT[0]+eT[1]),int(eT[3]+eT[4]),int(eT[6]+eT[7])
        res2 = (hr*3600) + (mi*60) + ss
        return res2 - res1