# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 1
        que=[(root,depth)]
        while que:
            for _ in range(len(que)):
                node,d = que.pop(0)
                if node.left: que.append((node.left,d+1))
                if node.right: que.append((node.right,d+1))
                depth = d
        return depth
