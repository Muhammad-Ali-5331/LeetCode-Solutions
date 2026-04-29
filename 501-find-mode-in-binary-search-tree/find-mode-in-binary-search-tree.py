# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        MAP = defaultdict(int)
        def ino(node):
            if node is not None:
                ino(node.left)
                ino(node.right)
                MAP[node.val]+=1
        ino(root)
        res = []
        mxF = max(list(MAP.values()))
        for k,v in MAP.items():
            if v==mxF:
                res.append(k)
        return res 