# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        v = root.val
        
        if p.val< v and q.val< v:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val >v and q.val>v:
            return self.lowestCommonAncestor(root.right, p, q)

        if p.val < v < q.val or q.val< v < p.val:
            return root

        else:
            return root

       
    