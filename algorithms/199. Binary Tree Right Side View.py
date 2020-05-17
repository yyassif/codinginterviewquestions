#DFS O(N) for space/run
class Solution(object):
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # depth -> node.val
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth, depth)

                # only insert into dict if depth is not already present.
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]

#BFS 
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        dic = {}
        max_level = -1
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop(0)  <---different from DFS
            if node is None:
                continue
            dic[level] = node.val     <---different from DFS : overwrite dictionary 
            max_level = max(max_level, level)
            stack.append((node.left, level+1))
            stack.append((node.right, level+1))
        return [dic[x] for x in range(max_level+1)]
    
