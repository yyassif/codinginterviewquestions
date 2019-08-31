#Myungho Sim
#kth smallest element from leetcode. using array and inorder. 
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
                preorder(node.left)
                # if node.val not in arr:
                arr.append(node.val)
                preorder(node.right)
        preorder(root)
        return arr[k-1]
