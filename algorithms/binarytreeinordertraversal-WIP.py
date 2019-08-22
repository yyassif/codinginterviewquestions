# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    arr=[]
    def __init__(self):
        arr=[]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr=[]
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            self.arr.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
        else:
            return None
        return self.arr
            
