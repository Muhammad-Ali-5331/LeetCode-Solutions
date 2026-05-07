class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = [[p,q]]
        while que:
            for _ in range(len(que)):
                node1,node2 = que.pop()
                if not node1 and not node2:
                    continue
                elif (node1 and not node2) or (node2 and not node1):
                    return False
                elif node1.val != node2.val: 
                    return False
                que.append([node1.left,node2.left])
                que.append([node1.right,node2.right])
                
        return True
        