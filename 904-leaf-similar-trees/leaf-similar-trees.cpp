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
    void io(TreeNode* node,vector<int>& arr){
        if (node!=nullptr){
           if (node->left == nullptr and node->right == nullptr){arr.push_back(node->val);}
           else{
            io(node->left,arr);
            io(node->right,arr);
           }
        }
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> arr1,arr2;
        io(root1,arr1);
        io(root2,arr2);
        return arr1 == arr2;
    }
};