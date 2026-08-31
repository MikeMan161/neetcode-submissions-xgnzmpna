# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        var = True
        def traverse(root: Optional[TreeNode]):
            nonlocal var

            if not root:
                return 0

            leftDepth = traverse(root.left)
            rightDepth = traverse(root.right)
            
            if abs(leftDepth - rightDepth) > 1:
                var = False
            
            return max(leftDepth, rightDepth) + 1
        traverse(root)
        return var
            

            