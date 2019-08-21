#Myungho Sim
#range sum bst from leetcode
#less efficient impl using preorder visit to every node. beats 5% of submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        v=0
        if root:
            if root.val>=L and root.val<=R:
                v= root.val
            l = self.rangeSumBST(root.left, L,R)
            if l<L and l>R:
                l=0
            r = self.rangeSumBST(root.right, L,R)
            if r<L and r>R:
                r=0
            return v+l+r
        else:
            return 0
            
#BST search algo, avoids visitng nodes outside of the range. beats 94% of submissions
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root:
            v = root.val
            if v<L:
                return self.rangeSumBST(root.right, L,R)
            elif v>R:
                return self.rangeSumBST(root.left, L,R)
            else:
                l = self.rangeSumBST(root.left, L,R)
                r = self.rangeSumBST(root.right, L,R)
                return v+l+r
        else:
            return 0
            
