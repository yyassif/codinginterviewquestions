# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(a, b):
            if a is None and b is None:
                return True
            elif a is None and b:
                return False
            elif a and b is None:
                return False
            return a.val==b.val or equals(a.left, b.left) or equals(a.right, b.right)
        def trav(a,b):
            return (a is not None) and (equals(a,b) or 
                                        trav(a.left, b.left) or
                                        trav(a.right, b.right))
        return trav(s,t)
