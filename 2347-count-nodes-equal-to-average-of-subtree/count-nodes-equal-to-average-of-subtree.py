# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def inord(node,Sum):
            if node is None: return 0,0
            lS,lC = inord(node.left,Sum)
            rS,rC = inord(node.right,Sum)
            currS = node.val + lS + rS
            totalNodes = lC+rC+1
            if (currS//totalNodes) == node.val: Sum[0]+=1
            return currS, totalNodes
        res = [0]
        inord(root,res)
        return res[0]