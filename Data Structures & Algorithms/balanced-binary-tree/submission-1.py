# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        temp = True
        def traverse(root):
            nonlocal temp
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            if max(left,right) - min(left, right) > 1:
                temp = False
        
            return max(left, right) + 1
        traverse(root)
        return temp