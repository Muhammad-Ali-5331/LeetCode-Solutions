class Solution {
public:
    int pairSum(ListNode* head) {
        stack<int> heads;
        int mx = 0;
        ListNode* temp = head;
        int n = 0;
        while (temp!=nullptr){heads.push(temp->val);temp = temp->next;n++;}
        int i = 0;
        int half = (n/2) - 1;
        temp = head;
        while (i<=half and temp!=nullptr){
            int top = heads.top();heads.pop();
            mx = max(mx, top + temp->val);
            temp = temp->next;
            i++;
        }
        return mx;
    }
};