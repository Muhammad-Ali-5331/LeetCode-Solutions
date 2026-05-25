class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordToLetter = {}
        letterToWord = {}
        words = s.split()
        n = len(words)
        if len(pattern)!=n: return False
        i = 0
        for ch in pattern:
            if i<n:
                if ch in letterToWord:
                    if letterToWord[ch]!=words[i]: return False
                elif words[i] in wordToLetter:
                    if wordToLetter[words[i]]!=ch: return False
                else:
                    letterToWord[ch] = words[i]
                    wordToLetter[words[i]] = ch
                i+=1
        return True