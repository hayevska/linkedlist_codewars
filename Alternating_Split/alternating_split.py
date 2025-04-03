class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    first_lst = []
    second_lst = []
    lst = []
    while head:
        lst.append(head.data)
        head = head.next
    for i, el in enumerate(lst):
        if i%2 == 0:
            first_lst.append(el)
        else:
            second_lst.append(el)
    first_lst.append(None)
    second_lst.append(None)
    first_lst, second_lst = first_lst[::-1], second_lst[::-1]
    for i in range(len(first_lst[:-1])):
        if i == 0:
            our_el = None
        else:
            our_el = first
        first = Node(first_lst[i+1])
        first.next = our_el
    first.data = first_lst[-1]
    for i in range(len(second_lst[:-1])):
        if i == 0:
            our_el = None
        else:
            our_el = second
        second = Node(second_lst[i+1])
        second.next = our_el
    second.data = second_lst[-1]
    return Context(first, second)
