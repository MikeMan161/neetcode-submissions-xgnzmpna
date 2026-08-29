# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def traverse(root: Optional[TreeNode]) -> int:
            nonlocal maxDiameter

            if not root:
                return 0
            
            leftDepth = traverse(root.left)
            rightDepth = traverse(root.right)

            if leftDepth + rightDepth > maxDiameter:
                maxDiameter = leftDepth + rightDepth
            
            return max(leftDepth, rightDepth) + 1        
        traverse(root)
        return maxDiameter

        
        
        