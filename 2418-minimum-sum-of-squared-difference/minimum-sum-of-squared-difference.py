class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        if k1 == 0 and k2 == 0: return sum(abs(nums1[i]-nums2[i])**2 for i in range(len(nums1)))
        HEAP = []
        MAP = defaultdict(int)
        for x,y in zip(nums1,nums2):
            diff = abs(x-y)
            if diff == 0: continue
            MAP[diff]+=1
            heappush(HEAP,(-diff))
        if not HEAP: return 0
        mod = True
        total = k1+k2
        while total and HEAP:
            # Get The Max Diff
            tp = abs(heappop(HEAP))
            
            #Get it's freq (the number of pairs having it)
            freq = MAP.get(tp,0)
            
            # It means this difference has been totally removed
            if freq == 0: continue
            
            #Get the min amount of pairs from which we can remove it
            to_use = min(total,freq)
            
            #It's the lower diff would be and add that amount of pairs we are decreasing
            lowerD = tp-1
            MAP[lowerD]+=to_use
            if lowerD>=0:
                heappush(HEAP,(-lowerD))

            #Subtract that amount from total difference
            total-= to_use

            #Subtract that from the freq of current largest diff
            freq -= to_use
            MAP[tp] = freq
        return sum((v**2)*f for v,f in MAP.items() if v>=0)