#Myungho Sim
#add two numbers problem @ leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2:
            return l2
        elif l1 and l2 is None:
            return l1
        sum =0
        value1=0
        value2=0
        i=0
        while l1:
            value1 = value1+l1.val*10**i
            i+=1
            l1 = l1.next
        i=0
        while l2:
            value2 = value2+l2.val*10**i
            i+=1
            l2 = l2.next
        sum = value1+value2
        #convert sum to array
        if sum==0:
            return ListNode(0)
        d = sum%10
        sum = sum//10
        head = ListNode(d)
        node = head
        while sum >0:
            d = sum%10
            sum = sum//10
            node.next = ListNode(d)
            node = node.next
        return head
