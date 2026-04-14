class Solution:
    def __init__(self):
        self.T = True
    def calchigh(self,node):
        if not node: return 0
        left = self.calchigh(node.left)
        right = self.calchigh(node.right)
        if abs(left-right) > 1:  self.T = False
        return max(left,right)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.calchigh(root)
        return self.T