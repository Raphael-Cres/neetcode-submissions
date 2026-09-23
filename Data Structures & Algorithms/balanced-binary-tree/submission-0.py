class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))

        if root is None:
            return True

        # Ta ligne parfaite ici :
        return (-1 <= maxDepth(root.left) - maxDepth(root.right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)