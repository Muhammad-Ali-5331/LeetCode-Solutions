class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0); // Standard dummy node pattern
        ListNode* current = dummy;
        int carry = 0;

        // One loop to rule them all: check l1, l2, OR if a carry is left
        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;

            // Logic: Calculate sum and new carry
            int sum = val1 + val2 + carry;
            carry = sum / 10;          // Integer division (e.g., 13 / 10 = 1)
            int digit = sum % 10;      // Modulo (e.g., 13 % 10 = 3)

            // Create new node and move forward
            current->next = new ListNode(digit);
            current = current->next;

            // Advance pointers if they aren't null
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        return dummy->next;
    }
};