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
    void pst(TreeNode* node, int &ts, string currN){
        if (node->left == nullptr and node->right == nullptr){ts+=stoi(currN + to_string(node->val));}
        else{
            if (node->left!=nullptr) pst(node->left,ts,currN+to_string(node->val));
            if (node->right!=nullptr) pst(node->right,ts,currN+to_string(node->val));
        }
    }
    int sumNumbers(TreeNode* root) {
        if (root == nullptr){ return 0;}
        int ts = 0;
        pst(root,ts,"");
        return ts;
    }
};