# level order iterative solution
from collections import deque
def serialize(self, root):
    dq = deque([root])
    ans = []
    while dq:
        node = dq.popleft()
        if node:
            ans.append(str(node.val))
            dq.append(node.left)
            dq.append(node.right)
        else:
            ans.append('')
    while ans and not ans[-1]:
        ans.pop()
    return ','.join(ans)

def deserialize(self, data):
    if not data:
        return None
    nodes = map(lambda s: None if not s else TreeNode(int(s)), data.split(','))
    nodes.reverse()
    root = nodes.pop()
    dq = deque([root])
    while nodes:
        node = dq.popleft()
        node.left = nodes.pop()
        if node.left:
            dq.append(node.left)
        if not nodes:
            break
        node.right = nodes.pop()
        if node.right:
            dq.append(node.right)
    return root
