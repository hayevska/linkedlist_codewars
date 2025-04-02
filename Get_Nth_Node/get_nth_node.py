class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    lst = []
    while node:
        lst.append(node.data)
        node = node.next
    if 0 <= index <= len(lst) - 1:
        output = Node(lst[index])
    else:
        raise Exception
    return output
