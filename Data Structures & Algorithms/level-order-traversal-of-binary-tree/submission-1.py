# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root):
            if not root:
                return []
            q = deque()
            q.append(root)
            final = []
            while q:
                length = len(q)
                i = 0
                temp = []
                while i < length:
                    cur = q.popleft()
                    temp.append(cur.val)

                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    i += 1
                final.append(temp)
                temp = []
            return final
        return traverse(root)
