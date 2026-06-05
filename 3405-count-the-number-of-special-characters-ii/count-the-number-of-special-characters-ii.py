from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        alreadyProcessed = set()
        processedLower = set()
        MAP = Counter(word)
        ans = 0
        for i in range(len(word)):
            MAP[word[i]] = max(0,MAP[word[i]]-1)
            if word[i] in alreadyProcessed: continue
            alreadyProcessed.add(word[i])
            if 'a'<=word[i]<='z': processedLower.add(word[i])
            else:
                l = chr(ord(word[i])+32)
                if not MAP[l] and l in processedLower: ans+=1
        return ans