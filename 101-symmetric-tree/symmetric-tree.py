# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        que = deque()
        que.append(root)
        while que:
            curr = []
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                    curr.append(node.left.val)
                else:
                    curr.append(None)
                if node.right:
                    que.append(node.right)
                    curr.append(node.right.val)
                else:
                    curr.append(None)
            if not(curr[:len(curr)//2] == curr[len(curr)//2:][::-1]):
                return False            
        return True