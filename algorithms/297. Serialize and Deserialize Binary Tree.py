# Serialize process run time O(T), space O(T)
# Deserialize process run time O(T), space O(1) (O(depth) including calling stack)
def __init__(self):
    self.data = []
    # self.inorder = []

def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur == None:
            self.data.append('#')
            continue
        self.data.append(cur.val)
        stack.append(cur.right)
        stack.append(cur.left)
    print(self.data)



def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    def build():
        if not self.data:
            return
        data = self.data.pop(0)
        if data == '#':
            return
        else:
            cur = TreeNode(data)
        cur.left = build()
        cur.right = build()
        return cur

    root = build()
    return root
    
    
    
