def is_bs(node):
    prevNode = Node()
    return _is_bs(node, prevNode)

def _is_bs(node, prevNode):
    if node == None:
        return True
    else:
        if _is_bs(node.left, prevNode):
            if prevNode.value == None or prevNode.value <= node.value:
                prevNode.value = node.value
            else:
                return False
        return _is_bs(node.right, prevNode)

class Node(object):
    def __init__(self,value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#n3 = Node()
#n2 = Node()
#n1 = Node()
#n5 = Node()
#n6 = Node()

#n3.value = 6
#n3.left = n2
#n3.right = n6
#n6.value = 6
#n2.value = 2
#n2.left = n1
#n2.right = n5
#n1.value = 1
#n5.value = 5

#answer = is_bs(n3)
#print answer