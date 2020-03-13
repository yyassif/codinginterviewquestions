def findMergeNode(head1, head2):
    node1 = head1
    node2 = head2

    while node1!=node2:
        if node1.next is None:
            node1=head1
        else:
            node1 = node1.next
        if node2.next is None:
            node2=head2
        else:
            node2 = node2.next
    return node1.data
