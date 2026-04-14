#include <queue>

class Solution {
public:
    struct compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val; // Min-heap logic
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, compare> pq;

        // Push the head of each list into the heap
        for (auto l : lists) { if (l) pq.push(l); }

        ListNode* dummy = new ListNode(0);
        ListNode* tail = dummy;

        while (!pq.empty()) {
            ListNode* top = pq.top();
            pq.pop();

            tail->next = top;
            tail = tail->next;

            // If there's a next node in the list we just popped from, add it to the heap
            if (top->next) pq.push(top->next);
        }
        return dummy->next;
    }
};