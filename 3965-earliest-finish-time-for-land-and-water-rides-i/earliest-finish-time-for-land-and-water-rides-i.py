from typing import List
class Solution:
    def earliestFinishTime(self, LS: List[int], LD: List[int], WS: List[int], WD: List[int]) -> int:
        l2 = len(WS)
        minT = float("inf")
        for i in range(len(LD)):
            landStart,landDuration = LS[i],LD[i]
            totalLandTime = landStart+landDuration
            for j in range(l2):
                waterStart,waterDuration = WS[j],WD[j]
                totalWaterTime = waterStart+waterDuration
                tLW = 0
                tWL = 0
                # Trying Land ---> Water
                if waterStart<=totalLandTime: 
                    tLW+=totalLandTime+waterDuration
                else: 
                    tLW+=totalWaterTime
                
                # Trying Water ---> Land
                if landStart<=totalWaterTime:
                    tWL+= totalWaterTime+landDuration
                else:
                    tWL+=totalLandTime
                minT = min(tLW,tWL,minT)
        return minT