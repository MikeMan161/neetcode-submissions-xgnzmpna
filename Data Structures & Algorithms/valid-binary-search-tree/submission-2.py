# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upperbound = float('inf')
        lowerbound = float('-inf')
        def traverse(root, upperbound, lowerbound):
            if not root:
                return True
            
            if lowerbound < root.val < upperbound:
                return traverse(root.left, root.val, lowerbound) and traverse(root.right, upperbound, root.val)
            else:
                return False

        return traverse(root, upperbound, lowerbound)