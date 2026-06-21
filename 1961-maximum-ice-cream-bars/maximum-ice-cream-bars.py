class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice = 0
        i = 0
        while i<len(costs):
            if coins<=0: break
            if coins-costs[i]>=0:
                coins-=costs[i]
                ice+=1
            i+=1
        return ice