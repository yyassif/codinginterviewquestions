#TODO
# * learn :construct binary tree from an array level order
# * learn :iterative inorder traversal using stack
#sol from hackerank discussions
import sys
sys.setrecursionlimit(2000)
class Node:
    def __init__(self, data, left, right):
        self.data = str(data)+' '
        self.left = None
        self.right = None

def inorderTraversal(root,s):
    if root:
        sl = inorderTraversal(root.left,s)
        sc = root.data
        sr = inorderTraversal(root.right,s)
        return sl+sc+sr
    else:
        return ''

def getDepth(root, depth):
    if root:
        dl = getDepth(root.left, depth+1)
        dr = getDepth(root.right, depth+1)
        depth = max(dl,dr)
    else:
        depth -= 1
    return depth

def swap(root, depth, height):
    if root:
        if depth == height:
            temp = root.left
            root.left = root.right
            root.right = temp
        else:
            swap(root.left, depth, height+1)
            swap(root.right, depth, height+1)
        

N = int(input())
Tree = [Node(i, None, None) for i in range(1, N+1)]
root = Tree[0]
for i in range(N):
    a, b = input().split(' ')
    a, b = [int(a)-1, int(b)-1]#Convert to zero index
    Tree[i].left = Tree[a] if a > 0 else None
    Tree[i].right = Tree[b] if b > 0 else None
depth = getDepth(root,1)
#print(inorderTraversal(root,''))
#print('depth',depth)
T = int(input())
for i in range(T):
    k = int(input())
    H = [k*i for i in range(1,N) if k*i <= depth]
    #print('H = ',H)
    for h in H:
        swap(root,h,1)
    print(inorderTraversal(root,''))
    #print('depth',depth)
    
#sol 2    
from collections import deque
class Node:
    def __init__(self, d):
        self.data = d
    
def build_tree(indexes):
    f = lambda x: None if x == -1 else Node(x)
    children = [list(map(f,x)) for x in indexes]
    nodes = {n.data: n for n in filter(None, sum(children, []))}
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        nodes[idx+1].left = child_pair[0]
        nodes[idx+1].right = child_pair[1]
    return nodes[1]

def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.data
            curr = curr.right
        
def swap_nodes(indexes, queries):
    root = build_tree(indexes)
    for k in queries:
        h = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % k == 0:
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            h += 1
        yield inorder(root)
