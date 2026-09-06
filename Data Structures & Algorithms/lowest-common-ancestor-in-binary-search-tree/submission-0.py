# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def isLCA (root: TreeNode, lower, upper):
            if lower <= int(root.val) <= upper:
                return root
            elif root.val < lower:
                return isLCA(root.right, lower, upper)
            elif root.val > upper:
                return isLCA(root.left, lower, upper)
        def traverse(root: TreeNode, p: TreeNode, q: TreeNode):
            lower = min(p.val, q.val)
            upper = max(p.val, q.val)


            return isLCA(root, lower, upper)
        return traverse(root, p, q)