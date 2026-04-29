# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([])
        q.append(root)
        while q:
            curr=  []
            for _ in range(len(q)):
                currNode = q.popleft()
                if currNode is None: continue
                q.append(currNode.left)
                q.append(currNode.right)
                curr.append(currNode.val)
            if curr:
                res.append(sum(curr)/len(curr))
        return res