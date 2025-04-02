class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return ' -> '.join(str(i) for i in self + ['None'])

def linked_list_from_string(s):
    """kkk"""
    if s == 'None':
        curr = None
    else:
        s_lst = s.split(' -> ')[::-1]
        for i in range(len(s_lst[:-1])):
            if i == 0:
                our_el = None
            else:
                our_el = curr
            curr = Node(int(s_lst[i+1]))
            curr.next = our_el
        curr.data = int(s_lst[-1])
    return curr
