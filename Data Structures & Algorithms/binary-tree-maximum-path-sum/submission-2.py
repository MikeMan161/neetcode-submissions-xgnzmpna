# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def traverse(root):
            nonlocal maxSum 
            
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            if (left + right + root.val) > maxSum:
                maxSum = (left + right + root.val)
            
            return max(left, right) + root.val

        traverse(root)
        return maxSum