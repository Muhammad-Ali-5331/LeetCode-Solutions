from typing import List
class Solution:  
    def earliestFinishTime(self, LS: List[int], LD: List[int], WS: List[int], WD: List[int]) -> int:
        LAND = sorted(list(zip(LS,LD)))
        WATER = sorted(list(zip(WS,WD)))
        landLen,waterLen = len(LD),len(WD)
        minT = float("inf")
        """ 
        # --- Step 1 --- # 
        # Trying Land --> Water
            For a fixed land ride, can I quickly find:
                The minimum waterDuration among rides with start ≤ landFinish
                The minimum (waterStart + waterDuration) among rides with start > landFinish
        # --- Step 2 --- #
        # Trying Water --> Land
            For a fixed water ride, can I quickly find:
                The minimum landDuration among rides with start ≤ waterFinish
                The minimum (landStart + landDuration) among rides with start > waterFinish
        """
        prefixWaterMinDuration,suffixWaterMin = [0]*waterLen,[0]*waterLen
        prefixWaterMinDuration[0],suffixWaterMin[-1] = WATER[0][1],WATER[-1][0]+WATER[-1][1]
        for i in range(1,waterLen):  prefixWaterMinDuration[i] = min(prefixWaterMinDuration[i-1],WATER[i][1])
        for i in range(waterLen-2,-1,-1): suffixWaterMin[i] = min(suffixWaterMin[i+1],WATER[i][0]+WATER[i][1])
        for ls,le in LAND:
            landFinish = ls+le    
            minInd = -1
            l,r = 0,waterLen-1
            # Search For start<=landFinish
            while l<=r:
                mid = (l+r)//2
                if WATER[mid][0]<=landFinish:
                    minInd = mid
                    l = mid+1
                else: r = mid-1
            if minInd!=-1: minT = min(minT,landFinish+prefixWaterMinDuration[minInd])
            minInd = -1
            l,r = 0,waterLen-1
            # Search For start>landFinish
            while l<=r:
                mid = (l+r)//2
                if WATER[mid][0]>landFinish:
                    minInd = mid
                    r = mid-1
                else: l = mid+1
            if minInd!=-1: minT = min(minT,suffixWaterMin[minInd])
        prefixLandMinDuration,suffixLandMin = [0]*landLen,[0]*landLen
        prefixLandMinDuration[0],suffixLandMin[-1] = LAND[0][1],LAND[-1][0]+LAND[-1][1]
        for i in range(1,landLen): prefixLandMinDuration[i] = min(prefixLandMinDuration[i-1],LAND[i][1])
        for i in range(landLen-2,-1,-1): suffixLandMin[i] = min(suffixLandMin[i+1],LAND[i][0]+LAND[i][1])
        for ws,we in WATER:
            waterFinish = ws+we
            minInd = -1
            l,r = 0,landLen-1
            while l<=r:
                mid = (l+r)//2
                if LAND[mid][0]<=waterFinish:
                    minInd = mid
                    l = mid+1
                else: r = mid-1
            if minInd!=-1: minT = min(minT,waterFinish+prefixLandMinDuration[minInd])
            minInd = -1
            l,r = 0,landLen-1
            while l<=r:
                mid = (l+r)//2
                if LAND[mid][0]>waterFinish:
                    minInd = mid
                    r = mid-1
                else: l = mid+1
            if minInd!=-1: minT = min(minT,suffixLandMin[minInd])
        return minT