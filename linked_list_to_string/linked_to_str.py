def stringify(node):
    output = []
    while node:
        output.append(str(node.data))
        node = node.next
    if node == None:
        output.append(str('None'))
    return ' -> '.join(output)
