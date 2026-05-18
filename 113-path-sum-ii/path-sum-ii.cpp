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
    void pthSum(TreeNode* root, int currSum,vector<int> currV,int &TS, vector<vector<int>> &res) {
        if (root->left == nullptr and root->right == nullptr) {
            if (currSum+root->val == TS) {
                currV.push_back({root->val});
                res.push_back(currV);
            }
        }
        else {
            currSum+=root->val;
            currV.push_back({root->val});
            if (root->left!=nullptr) pthSum(root->left,currSum,currV,TS,res);
            if (root->right!=nullptr)pthSum(root->right,currSum,currV,TS,res);
        }
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> res;
        if (root == nullptr){return res;}
        pthSum(root,0,{},targetSum,res);
        return res;
    }
};
