# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Length = 0
        temp = head
        while temp:
            temp = temp.next
            Length+=1
        temp = head
        prev = temp
        count = 1
        lastEnd = Length - n
        if lastEnd == 0:
            return head.next
        while temp:
            if count <= lastEnd:
                prev = temp
                temp = temp.next
                count+=1
            else:
                temp = temp.next
                prev.next = temp
                return head