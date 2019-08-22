#Myungho Sim
#Binary Tree Inorder Traversal
#faster than 92% of submissions on leetcode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                arr.append(root.val)
                if root.right:
                    inorder(root.right)
            else:
                return None
        inorder(root)
        return arr
