class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res = []
        n = len(s1)
        i = 0
        while i<n:
            if s1[i]!=s2[i]:
                st1,st2 = "",""
                while i<n and s1[i]!=s2[i]:
                    st1 += s1[i]
                    st2 += s2[i]
                    i+=1
                res.append([st1,st2])
            else: i+=1
        return res