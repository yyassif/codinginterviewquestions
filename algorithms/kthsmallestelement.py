#Myungho Sim
#kth smallest element from leetcode. using array and preorder. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        def preorder(node):
            if node:
                arr.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        arr.sort()
        return arr[k-1]
