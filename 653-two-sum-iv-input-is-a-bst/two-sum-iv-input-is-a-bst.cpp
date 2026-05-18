#include <bits/stdc++.h>
using namespace std;

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
    bool T(TreeNode* root, int &k,unordered_map<int,int> &MAP) {
        if (root == nullptr){return false;}
        if (MAP.contains(k-root->val)) return true;
        MAP[root->val] = 1;
        return T(root->left,k,MAP) or T(root->right,k,MAP);
    }
    bool findTarget(TreeNode* root, int k) {
        unordered_map<int,int> MAP;
        return T(root,k,MAP);
        
    }
};
