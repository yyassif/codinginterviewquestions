#Myungho Sim
#same tree problem @ leetcode
# ideas taken from leetcode discussion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p!=None and q==None:
            return False
        if p==None and q!=None:
            return False
        if p==None and q==None:
            return True
        check_left =False
        check_right = True
        if p!=None and q!=None:
            if p.val!=q.val:
                return False
            check_left = self.isSameTree(p.left, q.left)
            check_right = self.isSameTree(p.right, q.right)
        return check_left and check_right
