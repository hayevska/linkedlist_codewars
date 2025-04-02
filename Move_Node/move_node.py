class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source: Node, dest: Node):
    if not source:
        raise Exception
    dest1 = Node(source.data)
    dest1.next = dest
    source1 = source.next
    return Context(source1, dest1)
