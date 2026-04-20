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
    ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr || head->next == nullptr){return head;}
     ListNode* tem = new ListNode(0);
     ListNode* prev = tem;
     ListNode* p1 = head;
     ListNode* p2 = p1->next;
     while (p1!=nullptr){
        bool same = false;
        while (p2!=nullptr and p2->val == p1->val){
            same = true;
            p2 = p2->next;
        }
        if (!same){
            prev->next = p1;
            prev = p1;
            prev->next= nullptr;
        }
        p1 = p2;
        if (p1!=nullptr){ p2 = p1->next;}
     }
     return tem->next;
    }
};