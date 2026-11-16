class Solution:
    def digitSum(self, S: str, K: int) -> str:
        def help(s,k):
            res = ""
            n = len(s)
            i = 0
            while i<n:
                nxt = min(n,i+k)
                curr = 0
                while i<nxt:
                    curr += int(s[i])
                    i+=1
                res += str(curr)
            return res
        while len(S)>K:
            S = help(S,K)
        return S