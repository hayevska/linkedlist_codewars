class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head or not head.next:
        return head
    s_lst = []
    while head:
        s_lst.append(head.data)
        head = head.next
    s_lst = sorted(set(s_lst))
    s_lst.append(None)
    s_lst = s_lst[::-1]
    for i in range(len(s_lst[:-1])):
        if i == 0:
            our_el = None
        else:
            our_el = curr
        curr = Node(s_lst[i+1])
        curr.next = our_el
    curr.data = s_lst[-1]
    return curr
