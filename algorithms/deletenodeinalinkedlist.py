#Myungho Sim
#delete a node. no previous node given. A problem @ leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#better solution based on an idea taken from leetcode discussion. replace value with the next node and connect to next next node
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
#solution 2 - slower. shift entire rest of the linked list
# class Solution:
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#         while node.next:
#             node.val = node.next.val
#             prev = node
#             node = node.next
#         prev.next = None
