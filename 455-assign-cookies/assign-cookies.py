class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = 0
        j = 0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
                j+=1
                count+=1
            else: i+=1
        return count