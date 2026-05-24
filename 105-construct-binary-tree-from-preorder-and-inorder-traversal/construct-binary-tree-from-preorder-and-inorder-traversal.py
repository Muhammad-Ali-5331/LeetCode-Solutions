class Solution:
    def __init__(self):
        self.idx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        MAP = {}
        for ind,val in enumerate(inorder):
            MAP[val] = ind
        idx = 0
        def BT(start,end):
            if start > end: return None
            root = TreeNode(preorder[self.idx])
            self.idx+=1
            i = MAP.get(root.val)
            root.left = BT(start,i-1)
            root.right = BT(i+1,end)
            return root
        return BT(0,len(preorder)-1)