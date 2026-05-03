from collections import deque
from typing import List
class Solution:
    def calcDiff(self,str1,str2):
        diff = 0
        for i in range(len(str1)):
            diff+= str1[i]!=str2[i]
        return diff
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        if not endWord in wordList: return 0
        adjList = {key: [] for key in wordList}
        adjList.update({beginWord:[]})
        for i in range(n):
            currWord = wordList[i]
            for j in range(i+1,n):
                if self.calcDiff(currWord,wordList[j]) == 1:
                    adjList[currWord].append(wordList[j])
                    adjList[wordList[j]].append(currWord)
        visit = set()
        que = deque()
        for wrd in wordList:
            if self.calcDiff(beginWord,wrd) == 1: adjList[beginWord].append(wrd)
        que.append((beginWord,1))
        while que:
            currWord,currD = que.popleft()
            if currWord == endWord: return currD
            if currWord in visit: continue
            visit.add(currWord)
            for connectedWord in adjList[currWord]:
                if connectedWord in visit: continue
                que.append((connectedWord,currD+1))
        return 0