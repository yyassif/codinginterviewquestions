#Myungho Sim
#print singly linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListNodes(head):
  node = head
  while(node is not None):
    print(node.val)
    node = node.next
#initialize singly linked list nodes
node = ListNode(0)
head=node
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = None
printListNodes(head)
