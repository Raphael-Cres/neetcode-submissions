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
    int ans = INT_MIN;

    int dfs(TreeNode* node) {
        // Base case, null contributes 0 to a downward path
        if (!node) return 0;

        // Best downward contribution from left and right
        // Ignore negative paths by clamping at 0
        int leftGain = max(0, dfs(node->left));
        int rightGain = max(0, dfs(node->right));

        // Best path using this node as the highest point
        int pathThroughNode = node->val + leftGain + rightGain;

        // Update global maximum
        ans = max(ans, pathThroughNode);

        // Return best single-branch path upward to parent
        return node->val + max(leftGain, rightGain);
    }

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
