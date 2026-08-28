# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxD = 0
    temp = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.temp += 1
        self.maxDepth(root.left)

        if self.temp > self.maxD:
            self.maxD = self.temp

        self.maxDepth(root.right)
        self.temp -= 1

        return self.maxD