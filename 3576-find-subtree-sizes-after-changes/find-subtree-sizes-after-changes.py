from typing import List
import copy
from collections import defaultdict
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        res = [0]*n
        found = {chr(ord('a')+i): [] for i in range(26)}
        nodeLetter = dict()
        adjList = defaultdict(set)
        for i in range(n):
            nodeLetter[i] = s[i]
            if parent[i] == -1: continue
            adjList[parent[i]].add(i)
        copyAdj = copy.deepcopy(adjList)
        #print(f"Before Adj List: {adjList}")

        # We don't distrub the main copy and get the new copy at end
        def traverse(node,fnd,parent=None):
            nodeChar = nodeLetter.get(node) # Get the character of current Node
            fnd[nodeChar].append(node) # Add that to the current Found Character's Nodes
            for child in adjList[node]:
                childRes = traverse(child,fnd,node)
                if childRes: copyAdj[node].discard(child) # Remove in the Temp Copy as any deep child can be added in this parent
            fnd[nodeChar].pop()
            if fnd[nodeChar]:
                lastNode = fnd[nodeChar][-1]
                if lastNode == parent: return False
                copyAdj[lastNode].add(node) # Add in the Temp copy parent as well
                return True
            return False
        traverse(0,found)
        adjList = copyAdj.copy()
        #print(f"After Adj List: {adjList}")
        def updateSize(node,output):
            deepth = 1
            for child in adjList[node]:
                deepth += updateSize(child,output)
            output[node] = deepth
            return output[node]
        updateSize(0,res)
        return res