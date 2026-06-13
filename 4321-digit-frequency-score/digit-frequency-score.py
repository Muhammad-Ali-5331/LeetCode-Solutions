class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        res = 0
        MAP = Counter(str(n))
        for k,v in MAP.items():
            res+= int(k)*v
        return res