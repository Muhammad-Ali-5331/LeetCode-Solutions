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
    void po(TreeNode* node,unordered_set<int>& arr){
        if (node!=nullptr){
            arr.insert(node->val);
            po(node->left,arr);
            po(node->right,arr);
        }
    }
    bool isUnivalTree(TreeNode* root) {
        unordered_set<int> mySet;
        po(root,mySet);
        return mySet.size()<=1;
    }
};