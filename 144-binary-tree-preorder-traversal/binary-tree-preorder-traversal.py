# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,node,li):
        if node is not None:
            li.append(node.val)
            self.preorder(node.left,li)
            self.preorder(node.right,li)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        p = list()
        self.preorder(root,p)
        return p
