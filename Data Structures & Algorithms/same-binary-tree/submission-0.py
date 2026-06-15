# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p:
            if not q:
                return True
            return False
        
        elif p and q:
            if p.val == q.val:
                right = self.isSameTree(p.right, q.right)
                left = self.isSameTree(p.left, q.left)
                return right and left
            else:
                return False
        
        else:
            return False