# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head) :
        if not head: return head
        if not head.next: return head
        globalEvenPointer = head.next
        oddPointer = head
        evenPointer = head.next
        while evenPointer and evenPointer.next:
            oddPointer.next = evenPointer.next
            evenPointer.next = evenPointer.next.next
            oddPointer = oddPointer.next
            evenPointer = evenPointer.next
        oddPointer.next = globalEvenPointer
        return head