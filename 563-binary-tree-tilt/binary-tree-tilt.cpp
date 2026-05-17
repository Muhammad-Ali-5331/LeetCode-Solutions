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
    int tempF(TreeNode* root, int &s){
        if (root == nullptr) return 0;
        int l = tempF(root->left,s);
        int r = tempF(root->right,s);
        s+= abs(l-r);
        return root->val + l + r;
    }
    int findTilt(TreeNode* root) {
        int S = 0;
        tempF(root,S);
        return S;
    }
};