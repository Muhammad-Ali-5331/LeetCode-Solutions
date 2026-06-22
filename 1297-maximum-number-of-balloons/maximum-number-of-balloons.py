class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        MAP = Counter(text)
        bC = MAP.get('b',0)
        aC = MAP.get('a',0)
        nC = MAP.get('n',0)
        lC = MAP.get('l',0)//2
        oC = MAP.get('o',0)//2
        return min(bC,aC,nC,lC,oC)