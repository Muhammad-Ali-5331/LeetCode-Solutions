/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverse(int i,int k,int len,ListNode* node){
        if (i+k > len) return node;
        ListNode* before = nullptr;
        ListNode* temp = node;
        ListNode* after = nullptr;
        for (int j = 0; j<k;j++){
            after = temp->next;
            temp->next = before;
            before = temp;
            temp = after;
        }
        node->next = reverse(i+k,k,len,after);
        return before;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = 0;
        ListNode* temp = head;
        while (temp!=nullptr){
            len++;
            temp = temp->next;
        }
        return reverse(0,k,len,head);
    }
};