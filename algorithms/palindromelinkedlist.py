#Myungho Sim
#palindrome linked list problem from leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    cntback=0
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True
        node = head
        cnt=0
        map ={}
        while (node is not None):
            map[cnt]=node.val
            node = node.next
            cnt+=1
            
        for i in range(cnt):
            if map[i]!=map[cnt-1-i]:
                return False
        return True
