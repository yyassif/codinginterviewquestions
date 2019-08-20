#Myungho Sim
#greater sum tree @leet code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#idea taken from leetcode discussion. 
#single pass solution
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.greaterSum(root, 0)
        return root
    def greaterSum(self, root, sum):
        rootVal = root.val
        if root.right:
            right = self.greaterSum(root.right,sum)
        else:
            right=0
        root.val+=right + sum # in BST, right node is bigger
        if root.left:
            left =self.greaterSum(root.left, root.val)
        else:
            left=0
        return rootVal +right+left
# less efficient solution. 3 pass using a hashmap.
# class Solution:
#     map = {}
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         map = {}
#         self.buildMapOfTree(root)
#         for key in self.map:
#             value=0
#             for k,v in self.map.items():
#                 if key<=k:
#                    value+=k
#             self.map[key] = value
#             # print(value)
#         self.updateTreeValue(root)
#         # for k,v in self.map.items():
#         #     print (k,v)
#         # self.printTree(root)
#         return root
#     def buildMapOfTree(self,root):
#         if root:
#             self.map[root.val] = 0
#             self.buildMapOfTree(root.left)
#             self.buildMapOfTree(root.right)
#     def updateTreeValue(self,root):
#         if root:
#             root.val = self.map[root.val]
#             self.updateTreeValue(root.left)
#             self.updateTreeValue(root.right)
#     def printTree(self,root):
#         if root:
#             print(root.val)
#             self.printTree(root.left)
#             self.printTree(root.right)
