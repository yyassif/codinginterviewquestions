#Myungho Sim
#check cycles in linked list
#use fast and slow runner
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #check if head is None
        if head is None:
            return False
        #check if head points back to itself
        if head.next == head:
            return True
        slow = head
        fast = head
        #use slow and fast runner to check for cycles
        while slow and fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return False
            if slow == fast:
                return True
        return False
