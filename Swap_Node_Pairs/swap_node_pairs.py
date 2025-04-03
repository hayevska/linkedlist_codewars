class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head: Node):
    if not head or not head.next:
        return head
    prev = head
    curr = head.next
    head = curr
    while prev and curr:
        temp = curr.next
        if temp and temp.next:
            prev.next = temp.next
        else:
            prev.next = temp
        curr.next = prev
        prev = temp
        if temp:
            curr = temp.next
        else:
            curr = None
    return head
