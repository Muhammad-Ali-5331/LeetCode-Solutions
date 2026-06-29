class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        MAP = defaultdict(int)
        n = len(word)
        for i in range(n):
            currs = ""
            for j in range(i,n):
                currs+=word[j]
                MAP[currs]+=1
        count = 0
        for word in patterns:
            count += MAP[word]>=1
        return count