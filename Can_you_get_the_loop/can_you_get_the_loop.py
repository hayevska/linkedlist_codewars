class Node(object):
    def __init__(self):
        self.next = None

def loop_size(node):
    lst = []
    while node:
        if node in lst:
            lst = lst[lst.index(node):]
            break
        lst.append(node)
        node = node.next
    return len(lst)
