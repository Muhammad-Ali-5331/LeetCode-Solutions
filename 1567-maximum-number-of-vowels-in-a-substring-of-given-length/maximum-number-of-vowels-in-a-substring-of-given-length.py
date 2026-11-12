class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mxC = 0
        l,r = 0,0
        cVC = 0
        vowels = {'a', 'e', 'i', 'o','u'}
        while r < len(s):
            cVC += s[r] in vowels
            if r-l>=k:
                cVC -= s[l] in vowels
                l+=1
            mxC = max(mxC,cVC)
            r+=1
        return mxC