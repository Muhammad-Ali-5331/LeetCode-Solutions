class Solution {
public:
    TreeNode* flattenAndReturnTail(TreeNode* node) {
        if (!node) return nullptr;

        // If leaf node, it's already a flattened list of size 1
        if (!node->left && !node->right) {
            return node;
        }

        TreeNode* leftTail = flattenAndReturnTail(node->left);
        TreeNode* rightTail = flattenAndReturnTail(node->right);

        // If there is a left subtree
        if (node->left) {
            // Save original right subtree
            TreeNode* tempRight = node->right;

            // Move left subtree to right
            node->right = node->left;
            node->left = nullptr;

            // Attach original right subtree at the end of left subtree
            leftTail->right = tempRight;
        }

        // Return the last node (tail) of the flattened subtree
        if (rightTail) return rightTail;
        if (leftTail) return leftTail;
        return node;
    }

    void flatten(TreeNode* root) {
        flattenAndReturnTail(root);
    }
};