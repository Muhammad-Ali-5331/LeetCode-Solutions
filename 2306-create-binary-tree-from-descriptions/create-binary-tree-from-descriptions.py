# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def createBinaryTree(self, D: List[List[int]]) -> Optional[TreeNode]:
        MAP = {}
        for parent,child,flag in D:
            if parent not in MAP: MAP[parent] = [-1,-1]
            MAP[parent][0 if flag else 1] = child
        vals = set(MAP.keys())
        for li in MAP.values():
            vals.discard(li[0])
            vals.discard(li[1])
        def makeTree(currVal):
            if not currVal in MAP: 
                return TreeNode(currVal)
            root = TreeNode(currVal)
            if MAP[currVal][0]!=-1:
                root.left = makeTree(MAP[currVal][0])
            if MAP[currVal][1]!=-1:
                root.right = makeTree(MAP[currVal][1])
            return root
    
        rootVal = list(vals)[0]
        return makeTree(rootVal)