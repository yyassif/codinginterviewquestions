# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum =float('-inf')
        def rec(node):
            if node is None:
                return 0
            left= max(rec(node.left), 0)
            right = max(rec(node.right),0)
            #max path can extend from left to right thru the root node
            new_path = node.val+left+right
            self.max_sum = max(self.max_sum, new_path)
            return node.val+max(left, right)  #return only the maximum of left or right then add node's value to it
        rec(root)
        return self.max_sum
            
