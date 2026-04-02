def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if not head:
        return new_node
    
    dummy = head
    
    while dummy.next:
        dummy = dummy.next
    
    dummy.next = new_node
    
    return head