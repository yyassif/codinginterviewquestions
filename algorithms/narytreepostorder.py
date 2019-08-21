#Myungho Sim
#iterative solution using stack and recursive solution
#iterative sol - faster than 17% of submissions
#for both solutions, ideas were taken from leetcode discussions
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        ret = []
        while stack:
            curr = stack.pop()
            if curr:
                if curr.children:
                    for child in curr.children:
                        stack.append(child)
                ret.append(curr.val)
        return ret[::-1]
            
#recursive solution. idea taken from leetcode discussion. better than 43% of submissions.
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         if not root.children:
#             return [root.val]
#         sub= []
#         for child in root.children:
#             sub +=self.postorder(child)
#         return sub+ [root.val]
