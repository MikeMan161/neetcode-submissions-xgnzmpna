# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        temp = 0
        def traverse(root: Optional[TreeNode]):
            nonlocal temp
            nonlocal maxD

            if not root:
                return 0

            temp += 1
            traverse(root.left)

            if temp > maxD:
                maxD = temp

            traverse(root.right)
            temp -= 1
        traverse(root)
        return maxD