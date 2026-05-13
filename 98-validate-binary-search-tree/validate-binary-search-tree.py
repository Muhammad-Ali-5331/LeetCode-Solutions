class Solution:
    def validate(self,node,minAllowed,maxAllowed):
        if node is None: return True
        if minAllowed<node.val<maxAllowed:
            return self.validate(node.left,minAllowed,min(node.val,maxAllowed)) and self.validate(node.right,max(node.val,minAllowed),maxAllowed)
        else:
            return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float("-inf"),float("inf"))