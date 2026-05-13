# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque()
        que.append(root)
        result = []
        result.append([root.val])
        
        while que:
            curr = []
            n = len(que)
            for _ in range(n):
                node = que.popleft()
                if node.left:
                    curr.append(node.left.val)
                    que.append(node.left)
                if node.right:
                    curr.append(node.right.val)
                    que.append(node.right)
            if curr:
                result.append(curr)
        return result