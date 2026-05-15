class Solution:
    def isGood(self, nums: List[int]) -> bool:
        d = Counter(nums)
        rptN = len(set(nums))
        if not rptN in d: return False
        if d[rptN]!=2: return False
        for k,v in d.items():
            if v>=2 and k!=rptN: return False
        for i in range(1,rptN+1):
            if not i in d: return False
        return True