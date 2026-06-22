class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        MAP = Counter(text)
        count = 0
        word = "balloon"
        while True:
            for ch in word:
                if MAP.get(ch,0)>0:
                    MAP[ch] = max(0,MAP.get(ch,0)-1)
                else: return count
            count+=1