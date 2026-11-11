class Solution:
    def minimumCost(self, c1: int, c2: int, cB: int, n1: int, n2: int) -> int:
        res1 = 0
        o1,o2 = n1,n2
        if cB<=c1:
            res1 += n1*cB
            n2 -= min(n2,n1)
            n1 = 0
        if cB<=c2:
            res1 += n2*cB
            n1 -= min(n2,n1)
            n2 = 0
        res1 += n1*c1 + n2*c2
        res2 = 0
        mi = min(o1,o2)
        res2 += mi * cB
        o1-=mi
        o2-=mi
        res2 += o1 * c1
        res2 += o2 * c2
        return min(res1,res2)