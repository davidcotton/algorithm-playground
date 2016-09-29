
class LinkedList:
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

        def element(self):
            return self.element

        def get_next(self):
            return self.next

        def __repr__(self):
            return 'Node<{}>'.format(self.element)

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def empty(self):
        return self.len == 0

    def prepend(self, element):
        self.head = self.Node(element, self.head)

        if self.empty():
            self.tail = self.head

        self.len += 1

    def __repr__(self):
        result = ''
        if not self.empty():
            node = self.head
            result += str(node.element)
            node = node.get_next()
            while node:
                result += ', {}'.format(node.element)
                node = node.get_next()

        return 'LinkedList<{}>'.format(result)


ll = LinkedList()
ll.prepend(1)
ll.prepend(2)
ll.prepend(4)

print(ll)
