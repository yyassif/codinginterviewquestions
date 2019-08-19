#Myungho Sim
#intersection of two linked lists O(M+N), space = O(1)
#ideas taken from https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        anode = headA
        bnode = headB
        acnt=0
        bcnt=0
        #get length of each linked list
        while anode is not None:
            anode = anode.next
            acnt+=1
        while bnode is not None:
            bnode = bnode.next
            bcnt+=1
        diff = abs(acnt-bcnt)
        anode = headA
        bnode = headB
        #skip larger list diff times
        for i in range(diff):
            if acnt>bcnt:
                anode = anode.next
            else:
                bnode = bnode.next
        while anode is not None:
            if anode==bnode:
                return anode
            anode = anode.next
            bnode = bnode.next
        return None
        
            
