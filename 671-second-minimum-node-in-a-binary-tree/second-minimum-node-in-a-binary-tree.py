# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minVal = []
        def tr(node,mi):
            if node is not None:
                heappush(minVal,node.val)
                tr(node.left,mi)
                tr(node.right,mi)
        tr(root,minVal)
        mxVal = heappop(minVal)
        while minVal and minVal[0] == mxVal: heappop(minVal)
        return -1 if not minVal else abs(heappop(minVal))