#iterative sol runtime-O(n+m), storage-O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        copy_head = ListNode(-1)
        copy_node = copy_head
        while l1 and l2:
            if l1.val<=l2.val:
                copy_node.next =l1
                l1 =l1.next
            else:
                copy_node.next = l2
                l2 = l2.next
            copy_node = copy_node.next
        copy_node.next = l1 if l1 and not l2 else l2
        return copy_head.next
    
#recursive sol - runtime O(n+m), storage O(n+m) because of call stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return
        if l1 is None and l2:
            return l2
        if l1 and l2 is None:
            return l1
        if l1.val <=l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        elif l1.val >l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
            
