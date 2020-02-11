# 1->2->3->None
# 1<-2<-3<-None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        prev = None
        node = head
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev #last prev is the last Node at the end
