# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root and not subRoot:
                return True
            if root and not subRoot:
                return False
            if not root and subRoot:
                return False
            if root and subRoot:
                if root.val != subRoot.val:
                    return False
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        def traverse(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root:
                return False
            else:
                return isSameTree(root, subRoot) or traverse(root.left, subRoot) or traverse(root.right, subRoot)
        
        return traverse(root, subRoot)


        
