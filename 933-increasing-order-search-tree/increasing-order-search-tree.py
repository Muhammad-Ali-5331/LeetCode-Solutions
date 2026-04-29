# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = TreeNode()
        def fi(node,dumm):
            if node is not None:
                dumm.val = node.val
                fi(node.left,dumm)
        fi(root,d)
        nodes = []
        def io(node,cu):
            if node is not None:
                cu.append(node)
                io(node.left,cu)
                io(node.right,cu)
        io(root,nodes)
        nodes.sort(key=lambda x: x.val)
        currD = d
        for i in range(len(nodes)):
            curr = nodes[i]
            if curr.val == d.val: continue
            curr.left = curr.right = None
            currD.right = curr
            currD = currD.right
            i+=1
        return d