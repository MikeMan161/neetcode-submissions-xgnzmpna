# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def traverse(root):
            nonlocal maxDiameter
            
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            maxDiameter = max((left + right), maxDiameter)

            return max(left, right) + 1

        traverse(root)
        return maxDiameter