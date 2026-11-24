class Solution:
    def maxLength(self, arr: List[int]) -> int:
        mx = 1
        n = len(arr)
        for l in range(n):
            cl = arr[l]
            cg = arr[l]
            cp = 1
            for r in range(l,n):
                cl = lcm(cl,arr[r])
                cg = gcd(cg,arr[r])
                cp*=arr[r]
                if cp == (cl*cg): mx = max(mx,r-l+1)
        return mx