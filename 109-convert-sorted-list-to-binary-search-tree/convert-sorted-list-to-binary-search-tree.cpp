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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sorted_arr_to_bst(int l,int r,vector<int>& nums) {
            if (l>r) {return nullptr;} // Base Case for root->right Traversal
            if (l==r){return new TreeNode(nums[l]);} // Base Case for root->left traversal
            int mid = l+(r-l)/2;
            TreeNode* root = new TreeNode(nums[mid]);
            root->left = sorted_arr_to_bst(l,mid-1,nums);
            root->right = sorted_arr_to_bst(mid+1,r,nums);
            return root;
        }
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> nums;
        ListNode* temp = head;
        while (temp!=nullptr){nums.push_back(temp->val);temp=temp->next;}
        sort(nums.begin(),nums.end());
        return sorted_arr_to_bst(0,nums.size()-1,nums);
    }
};