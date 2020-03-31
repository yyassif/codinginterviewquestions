##iterative, O(1) storage sol
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:
            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next   #A->A'->B
            ptr.next = new_node        #A->A'
            ptr = new_node.next        #ptr =B

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            # A->A'->B->B' ptr.next is A' if ptr.random is C, ptr.random.next is C'
            ptr.next.random = ptr.random.next if ptr.random else None  
            ptr = ptr.next.next #get next ptr. A->A'->B->B'

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        node = head # A->B->C
        new_head = new_node = head.next # A'->B'->C'
        while node:
            if node.next:
                node.next = node.next.next #jump A' to A->B
            if new_node.next:
                new_node.next = new_node.next.next if new_node.next else None jump B to A'->B'
            node = node.next
            new_node = new_node.next  #jump to the next pointer
        return new_head




#######END OF O(1) sol

########### ITERATIVE SOL
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
