def has_cycle(head):
    fast = slow = head
    if slow:
        slow = slow.next
    if fast.next:
        fast = fast.next.next
    while slow and fast:
        if slow.data==fast.data:
            return True
        if fast.next:
            fast = fast.next.next
        slow = slow.next
    return False
