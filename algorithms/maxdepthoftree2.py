#Myungho Sim
#Max depth of a tree from leetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        a =1
        b=1
        if root.left is not None:
            a = self.maxDepth(root.left)+1
        if root.right is not None:
            b = self.maxDepth(root.right)+1
        return a > b and a or b
