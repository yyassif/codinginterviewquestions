# 337.houserobber3.
# sol from https://leetcode.com/problems/house-robber-iii/discuss/472740/Python-O(n)-DFSDP-Explanation-and-Commented-Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        def trav(node):
            if node is None:
                return (0,0)
            if node.left is None and node.right is None:
                return (node.val,0)
            if node.left and node.right:
                left = trav(node.left)
                right = trav(node.right)
                curr = left[0]+right[0]+node.val
                prev = max(left[0]+right[1], left[0]+right[0],left[1]+right[0], left[1]+right[1])
                return (curr, prev)
            elif node.right:
                right = trav(node.right)
                curr = right[1]+node.val
                prev = max(right[0], right[1])
                return (curr, prev)
            elif node.left:
                left = trav(node.left)
                curr = left[1]+node.val
                prev = max(left[0], left[1])
                return (curr, prev)
        curr, prev = trav(root)
        # print(curr, prev)
        return max(curr, prev)
