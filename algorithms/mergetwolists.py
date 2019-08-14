# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return None
        head = None
        if l1.val < l2.val:
            head = l1
        else:
            head = l2
        curr=None
        next = None
        while l1 is not None and l2 is not None:
            if l1.vla < l2.val:
                curr = l1
                if l1.next.val <l2.val:
                    next = l1.next
                else:
                    next = l2
            else:
                curr =l2
                if l1.next.val <l2.val:
                    next = l1.next
                else:
                    next = l2
            
            curr.next = next
            curr = next
        if l1 is None and l2 is not None:
            l2 = l2.next
        elif l1 is not None and l2 is None:
            l1=l1.next
        return head
            
                
            
            
