class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        res = 0
        pN,dN = len(prices),len(discounts)
        i,j = 0,0
        while i<pN and j<dN:
            res += (prices[i] * (100-discounts[j]))/100
            i,j = i+1,j+1
        while i<pN: 
            res += prices[i]
            i+=1
        return res