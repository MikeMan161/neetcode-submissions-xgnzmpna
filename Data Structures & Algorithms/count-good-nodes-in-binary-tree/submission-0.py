# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        maxv = root.val
        def dfs(root, maxv):
            nonlocal result
            if not root:
                return

            if root.val >= maxv:
                result += 1
                maxv = root.val
            
            dfs(root.left, maxv)
            dfs(root.right, maxv)

            return
        dfs(root,maxv)
        return result