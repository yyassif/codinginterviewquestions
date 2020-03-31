#https://leetcode.com/problems/invert-binary-tree/discuss/360867/Python3-recursively-and-iteratively
#Recursively:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        r =  self.invertTree(root.right)
        l =  self.invertTree(root.left)
        root.right =l
        root.left= r
        return root
#Iteratively BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            temp = cur.right
            cur.right = cur.left
            cur.left = temp
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root
