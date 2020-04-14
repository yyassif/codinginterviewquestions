# Serialize process run time O(T), space O(T)
# Serialize tree by DFS and preorder traversal
# e.g. [1,2,3,null,null,4,5]
# e.g. encode tree to 1,2,None,None,3,4,None,None,5,None,None
# Deserialize process run time O(T), space O(1) (O(depth) including calling stack)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node==None:
                arr.append("None")
                continue
            else:
                arr.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ','.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        # print(arr)
        def build():
            if arr is None:
                return
            val = arr.pop(0)
            if val=="None":
                return
            else:
                node = TreeNode(val)
            node.left = build()
            node.right = build()
            return node
        return build()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
    
    
    
