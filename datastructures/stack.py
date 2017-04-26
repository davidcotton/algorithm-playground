"""
    A stack is a collection of objects that are inserted and removed
    according to the "last-in first-out" (LIFO) principle.
"""

from abc import ABC, abstractmethod


class Stack(ABC):
    """A Stack interface."""
    @abstractmethod
    def __init__(self, *args):
        for arg in args:
            self.push(arg)

    @abstractmethod
    def push(self, e):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ArrayStack(Stack):
    """
    The array stack uses an array (or in Python's case a list) to hold its integers.
    As it's Python we don't need to worry about dynamically resizing the list as it grows.
    """
    def __init__(self, *args):
        self.size = 0
        self.data = []
        super().__init__(*args)

    def __repr__(self):
        result = ', '.join(str(x) for x in self.data)
        return '<{}>'.format(result)

    def push(self, e):
        """Adds an element to the top of the stack."""
        self.data.append(e)
        self.size += 1

    def pop(self):
        """Removes and returns the top element from the stack."""
        if self.empty():
            return None
        self.size -= 1
        return self.data.pop()

    def top(self):
        """Returns the top element of the stack without removing it."""
        if self.empty():
            return None
        return self.data[self.size]

    def size(self):
        """Returns the number of elements in the stack."""
        return self.size

    def empty(self):
        """Returns whether the stack is empty."""
        return self.size == 0


class LinkedStack(Stack):
    """
    This linked stack uses a linked list to store its integers.
    """
    class Node:
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'Node<{}>'.format(self.element)

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

    def __init__(self, *args):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.size = 0
        super().__init__(*args)

    def __repr__(self):
        result = ''
        if not self.empty():
            node = self.head
            result += str(node.element)
            node = node.get_next()
            while node:
                result += ', {}'.format(node.element)
                node = node.get_next()

        return 'Stack<{}>'.format(result)

    def push(self, e):
        """Adds an element to the top of the stack."""
        self.head = self.Node(e, self.head)
        self.size += 1

    def pop(self):
        """Removes and returns the top element from the stack."""
        # if self.is_empty():
        #     return None
        # self.size -= 1
        # return self.integers.pop()

    def top(self):
        """Returns the top element of the stack without removing it."""
        # if self.is_empty():
        #     return None
        # return self.integers[self.size]

    def size(self):
        """Returns the number of elements in the stack."""
        return self.size

    def empty(self):
        """Returns whether the stack is empty."""
        return self.size == 0


if __name__ == '__main__':
    stack = ArrayStack()
    # stack = LinkedStack()
    print(stack)
    stack.push(1)
    print(stack)
    stack.push(2)
    print(stack)
    stack.push(3)
    print(stack)
    stack.push(4)
    print(stack)
    stack.pop()
    print(stack)
