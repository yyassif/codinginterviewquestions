#Myungho Sim
#max depth of a n-ary tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root and root.children:
            arr=[]
            for child in root.children:
                c = self.maxDepth(child)
                arr.append(c)
                arr.sort(reverse=True)        
            return arr[0]+1
        else:
            return 1
#dfs solution - idea taken from leetcode discussions    
#class Solution:
#     def maxDepth(self, root: 'Node') -> int:
#         if not root:
#             return 0
#         return 1 + self.depth(root)
        
#     def depth(self, root):
#         if root and root.children:
#             return 1 + max([self.depth(child) for child in root.children])
#         else:
#             return 0
