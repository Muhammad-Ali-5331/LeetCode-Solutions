class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1,p2 = 0,0
        s1,s2 = len(s),len(t)
        while p1 < s1 and p2 < s2:
            if t[p2] == s[p1]:
                while p1 < s1 and p2 < s2 and t[p2] == s[p1]:
                    p1+=1
                    p2+=1
            else: p2+=1
        return p1 == s1