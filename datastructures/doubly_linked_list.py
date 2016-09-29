
class DoublyLinkedList:
    class Node:
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

        def element(self):
            return self.element

        def get_prev(self):
            return self.prev

        def get_next(self):
            return self.next

        def set_prev(self, prev):
            self.prev = prev

        def set_next(self, next):
            self.next = next

        def __repr__(self):
            return 'Node<{}>'.format(self.element)

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
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


ll = DoublyLinkedList()
ll.prepend(1)
ll.prepend(2)
ll.prepend(4)

print(ll)
