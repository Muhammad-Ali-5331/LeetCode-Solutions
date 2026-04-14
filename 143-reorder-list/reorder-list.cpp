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
    void reorderList(ListNode* head) {
        deque<ListNode*> pointers;
        ListNode* temp = head;
        while (temp!=nullptr){pointers.push_back(temp);temp = temp->next;}
        vector<ListNode*> res;
        while (!pointers.empty()){
            res.push_back(pointers.front());pointers.pop_front();
            if (!pointers.empty()){
                res.push_back(pointers.back());pointers.pop_back();
            }
        }
        for (int i = 0; i < (int)res.size() - 1; i++) {
            res[i]->next = res[i + 1];
        }
        
        // 4. Set the last node's next to NULL to avoid cycles
        res.back()->next = nullptr;
        head =res[0];
    }
};