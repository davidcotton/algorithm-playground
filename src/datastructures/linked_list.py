"""Linked lists."""

from abc import ABC, abstractmethod


class LinkedList(ABC):
    @abstractmethod
    def __init__(self, *args):
        self.len = 0
        for arg in args:
            self.prepend(arg)

    def is_empty(self) -> bool:
        return self.len == 0

    @abstractmethod
    def prepend(self, element):
        pass

    def __repr__(self):
        result = ''
        if not self.is_empty():
            node = self.head
            result += str(node.element)
            node = node.get_next()
            while node:
                result += ', {}'.format(node.element)
                node = node.get_next()
        return '{}<{}>'.format(self.__class__.__name__, result)

    def __len__(self):
        return self.len


class SinglyLinkedList(LinkedList):
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

    def __init__(self, *args):
        self.head = None
        self.tail = None
        super().__init__(*args)

    def prepend(self, element):
        self.head = self.Node(element, self.head)
        if self.is_empty():
            self.tail = self.head
        self.len += 1


class DoublyLinkedList(LinkedList):
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

    def __init__(self, *args):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        super().__init__(*args)

    def prepend(self, element):
        node = self.Node(element, None, self.head)
        if self.is_empty():
            self.tail = self.head
        else:
            self.head.next = node
        self.head = node
        self.len += 1


if __name__ == '__main__':
    # ll = SinglyLinkedList()
    ll = DoublyLinkedList()
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(4)
    print(ll)
