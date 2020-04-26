#Tip
# * It's known that inorder traversal of BST is an array sorted in the ascending order.
#    - reason why either left middle or right middle can be chosen as the root node
#    - left middle = (left+right)//2, right mid = (left+right)//2 plus one if odd
# * the tree should be height-balanced

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def helper(left, right): #left and right are only indexes
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        
        return helper(0, len(nums) - 1)
