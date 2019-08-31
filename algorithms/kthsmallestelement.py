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
        def inorder(node):
            if node:
                inorder(node.left)
                # if node.val not in arr:
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        return arr[k-1]
