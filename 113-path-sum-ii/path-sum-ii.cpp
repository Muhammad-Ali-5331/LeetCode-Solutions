#include <bits/stdc++.h>
using namespace std;
// struct TreeNode {
//       int val;
//       TreeNode *left;
//       TreeNode *right;
//       TreeNode() : val(0), left(nullptr), right(nullptr) {}
//       TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//       TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };
class Solution {
public:
    void pthSum(TreeNode* root,vector<int> currV,int TS, vector<vector<int>> &res) {
        if (root->left == nullptr and root->right == nullptr) {
            if (TS-root->val == 0) {
                currV.push_back({root->val});
                res.push_back(currV);
            }
        }
        else {
            currV.push_back({root->val});
            if (root->left!=nullptr) pthSum(root->left,currV,TS-root->val,res);
            if (root->right!=nullptr)pthSum(root->right,currV,TS-root->val,res);
        }
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> res;
        if (root == nullptr){return res;}
        pthSum(root,{},targetSum,res);
        return res;
    }
};
