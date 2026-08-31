# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        var = True
        
        def traverse(p: Optional[TreeNode], q: Optional[TreeNode]):
            nonlocal var
            if not p and not q:
                return
            elif p and not q:
                var = False
                return
            elif not p and q:
                var = False
                return
            elif p and q:
                if p.val != q.val:
                    var = False
                    return


            traverse(p.left, q.left)
            traverse(p.right, q.right)
        
        traverse(p,q)
        return var