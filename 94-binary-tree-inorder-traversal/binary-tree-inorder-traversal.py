# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node,li):
        if node is not None:
            self.inorder(node.left,li)
            li.append(node.val)
            self.inorder(node.right,li)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = list()
        self.inorder(root,p)
        return p