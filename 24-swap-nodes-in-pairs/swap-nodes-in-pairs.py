# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        def rec(node):
            if not node: return None
            curr = node
            nxt = node.next
            if nxt:
                recN = rec(nxt.next)
                curr.next = recN
            if nxt: nxt.next = curr
            return nxt if nxt else curr
        return rec(head)