class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data}, {repr(self.next)})'

def push(head: Node, data):
    curr = Node(data)
    curr.next = head
    return curr

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)
