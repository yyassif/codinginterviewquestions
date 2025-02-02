#Myungho Sim
# leetcode merge two lists problem
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(-1)
        prev = head
        while l1 and l2:
            if l1.val<=l2.val:
                prev.next = l1
                l1=l1.next
            else:
                prev.next = l2
                l2= l2.next
            prev= prev.next
        prev.next= l1 or l2
        return head.next
