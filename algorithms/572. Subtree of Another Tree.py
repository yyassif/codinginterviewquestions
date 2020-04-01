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
            elif a is None or b is None:
                return False
            return a.val==b.val and equals(a.left, b.left) and equals(a.right, b.right)
        def trav(a,b): #only one needs to branch off for comparison
            return (a is not None) and (equals(a,b) or 
                                        trav(a.left, b) or #it's just b, not b.left
                                        trav(a.right, b))  
        return trav(s,t)
