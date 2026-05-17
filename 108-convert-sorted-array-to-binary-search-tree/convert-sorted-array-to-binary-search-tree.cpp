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
    TreeNode* sorted_arr_to_bst(int l,int r,vector<int>& nums) {
        if (l>r) {return nullptr;} // Base Case for root->right Traversal
        if (l==r){return new TreeNode(nums[l]);} // Base Case for root->left traversal
        int mid = l+(r-l)/2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = sorted_arr_to_bst(l,mid-1,nums);
        root->right = sorted_arr_to_bst(mid+1,r,nums);
        return root;
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {return sorted_arr_to_bst(0,nums.size()-1,nums);}
};
