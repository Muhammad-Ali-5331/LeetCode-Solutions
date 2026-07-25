class Solution:
    def maxProduct(self, n: int) -> int:
        d = sorted(list(map(int,list(str(n)))),reverse=True)
        mx = 0
        L = len(d)
        for i in range(L):
            for j in range(i+1,L):
                mx = max(mx,d[i]*d[j])
        return mx