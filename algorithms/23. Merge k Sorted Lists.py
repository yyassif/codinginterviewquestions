#sol using priorityqueue runtime-O(nlogk) k=num of lists, space = O(n) creating new linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q=[]
        n = len(lists)
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(q,(l.val,i, l))
        node =head = ListNode(None)
        while q:
            _,i,node.next = heapq.heappop(q)
            node = node.next
            if node.next:
                heapq.heappush(q, (node.next.val,i,  node.next))
        return head.next
