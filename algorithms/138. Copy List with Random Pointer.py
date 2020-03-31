"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.map = {}   #key=original node, val= copied node, same with recursive sol. 
    def getNode(self,node):
        if node:
            if node in self.map:
                return self.map[node]
            else:
                self.map[node] = Node(node.val, None, None)
                return self.map[node]
        return None
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        node = head
        copy = Node(head.val, None, None)
        self.map[node] = copy
        while node is not None:
            copy.next = self.getNode(node.next)
            copy.random = self.getNode(node.random)
            copy = copy.next
            node = node.next
        return self.map[head]
