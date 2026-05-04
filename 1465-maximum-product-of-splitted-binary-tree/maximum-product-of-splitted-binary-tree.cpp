#include <bits/stdc++.h>
using namespace std;
// struct TreeNode {
//     int val;
//     TreeNode *left,*right;
//     TreeNode(int x):val(x),left(nullptr),right(nullptr){}
// };
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
    int postOrd(TreeNode *root,long long& mxVal,long long& TS) {
        if (root == nullptr) return 0;
        int left = postOrd(root->left,mxVal,TS);
        int right = postOrd(root->right,mxVal,TS);
        mxVal = max(mxVal,left * (TS-left));
        mxVal = max(mxVal,right * (TS-right));
        return root->val + left + right;
    }
    long long ts(TreeNode *root, long long& S) {
        if (root == nullptr) return 0;
        int left = ts(root->left,S);
        int right = ts(root->right,S);
        S = root->val + left + right;
        return root->val + left + right;
    }
    int maxProduct(TreeNode* root) {
        long long mx = INT_MIN;
        long long totalSum = 0;
        ts(root,totalSum);
        postOrd(root,mx,totalSum);
        long long MOD = pow(10,9)+7;
        return mx % MOD;
    }
};