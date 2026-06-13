class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        resMAP = {}
        for i in range(26):
            resMAP[i] = chr(ord('z')-i)
        weighMAP = {}
        for i in range(26):
            weighMAP[chr(ord('a')+i)] = weights[i]
        res = ""
        for word in words:
            currW = 0
            for ch in word: currW+= weighMAP[ch]
            res += resMAP[currW%26]
        return res
        