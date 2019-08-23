#Myungho Sim
#binary search inorder traversal. iterative and recursive methods.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ret.append(node.val)
                root = node.right
        return ret
#recursive solution        
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         arr = []
#         def inorder(root):
#             if root:
#                 if root.left:
#                     inorder(root.left)
#                 arr.append(root.val)
#                 if root.right:
#                     inorder(root.right)
#             else:
#                 return None
#         inorder(root)
#         return arr
