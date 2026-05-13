class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        que = deque([])
        leftToRight = True
        que.append(root)
        while que:
            curr = []
            for _ in range(len(que)):
                node = que.popleft()
                if not node: continue
                curr.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            if not leftToRight: curr = curr[::-1]
            if curr: res.append(curr)
            leftToRight = not leftToRight
        return res