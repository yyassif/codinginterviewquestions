def levelOrder(root):
    #Write your code here
    q = [] #use queue, not stack
    q.append(root)
    while q:
        node = q.pop(0) #QUEUE: FIFO pop left to right
        if node:
            print(node.info, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
