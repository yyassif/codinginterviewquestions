#recursive sol



#iterative sol
def lca(root, v1, v2):
    while(root != None):
        if(v1 > root.info and v2 > root.info):
            root = root.right
        elif(v1 < root.info and v2 < root.info):
            root = root.left
        else:
            break
    return root
