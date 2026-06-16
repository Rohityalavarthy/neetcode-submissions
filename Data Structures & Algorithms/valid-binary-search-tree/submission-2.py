class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            left  = validate(node.left,  min_val,    node.val)
            right = validate(node.right, node.val,   max_val)
            return left and right
        
        return validate(root, float('-inf'), float('inf'))