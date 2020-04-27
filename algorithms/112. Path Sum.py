# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sumv: int) -> bool:
        if root is None:
            return False
        
        def helper(node,sump=0):
            if node.left is None and node.right is None and node.val+sump==sumv:
                return True
            left_found=False
            right_found=False
            if node.left:
                left_found= helper(node.left,sump+node.val)
            if node.right:
                right_found = helper(node.right,sump+node.val)
            return left_found or right_found
        return helper(root)
        
