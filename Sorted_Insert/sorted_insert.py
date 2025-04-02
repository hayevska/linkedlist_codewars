class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head: Node, data):
    output = []
    while head:
        output.append(head.data)
        head = head.next
    output.append(data)
    output = sorted(output)
    output.append(None)
    output = output[::-1]
    for i in range(len(output[:-1])):
        if i == 0:
            our_el = output[i]
        else:
            our_el = curr
        curr = Node(output[i+1])
        curr.next = our_el
    curr.data = output[-1]
    return curr
