"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        curr = head
        while curr:
            temp = None
            currNext = curr.next
            if curr.child:
                nxt = curr.child
                nxt.prev = curr
                curr.child = None
                curr.next = nxt
                temp = self.flatten(nxt)
                while temp and temp.next: temp = temp.next
            if currNext and temp:
                temp.next = currNext
                currNext.prev= temp
            curr = curr.next
        return head