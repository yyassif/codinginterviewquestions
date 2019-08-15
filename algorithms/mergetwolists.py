#Myungho Sim
# leetcode merge two lists problem
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
        curr= ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next =l2
                curr = l2
                l2 = l2.next
        if l1 is None and l2 is not None:
            curr.next = l2
        elif l1 is not None and l2 is None:
            curr.next = l1
        return head
