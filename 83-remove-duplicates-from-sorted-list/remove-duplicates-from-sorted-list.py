# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeDP(self,head):
        mp = set()
        if head is None:
            return None
        current_node = head
        while current_node and current_node.next:
            if not current_node.val in mp: 
                mp.add(current_node.val)
            if not current_node.next.val in mp:
                current_node = current_node.next
            else:
                current_node.next = current_node.next.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.removeDP(head)
        return head
        