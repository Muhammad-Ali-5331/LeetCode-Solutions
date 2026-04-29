# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def pr(node):
            if node is not None:
                if node.val == target.val: return (node,True)
                resL = pr(node.left)
                if resL[1]: return (resL[0],True)
                resR = pr(node.right)
                if resR[1]: return (resR[0],True)
            return (None,False)
        r = pr(cloned)
        return r[0]