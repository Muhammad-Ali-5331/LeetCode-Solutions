class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()
        while list1 and list2:
            if list2.val < list1.val:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            else:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummy.next