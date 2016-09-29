class ArrayStack:
    """
    A stack is a collection of objects that are inserted and removed
    according to the "last-in first-out" (LIFO) principle.

    The array stack uses an array (or in Python's case a list) to hold its data.
    As it's Python we don't need to worry about dynamically resizing the list as it grows.
    """

    def __init__(self):
        self.size = 0
        self.data = []

    def __repr__(self):
        result = ', '.join(str(x) for x in self.data)
        return '<{}>'.format(result)

    def push(self, e):
        """Adds an element to the top of the stack."""
        self.data.append(e)
        self.size += 1

    def pop(self):
        """Removes and returns the top element from the stack."""
        if self.is_empty():
            return None
        self.size -= 1
        return self.data.pop()

    def top(self):
        """Returns the top element of the stack without removing it."""
        if self.is_empty():
            return None
        return self.data[self.size]

    def size(self):
        """Returns the number of elements in the stack."""
        return self.size

    def is_empty(self):
        """Returns whether the stack is empty."""
        return self.size == 0


class LinkedStack:
    """
    A stack is a collection of objects that are inserted and removed
    according to the "last-in first-out" (LIFO) principle.

    Uses a linked list to store its data.
    """

    class Node:
        def __init__(self, e):
            self.e = e

        def __repr__(self):
            return '<{}>'.format(self.e)

    def __init__(self):
        self.size = 0
        self.data = []

    def __repr__(self):
        result = ', '.join(str(x) for x in self.data)
        return '<{}>'.format(result)

    def push(self, e):
        """Adds an element to the top of the stack."""
        self.data.append(e)
        self.size += 1

    def pop(self):
        """Removes and returns the top element from the stack."""
        if self.is_empty():
            return None
        self.size -= 1
        return self.data.pop()

    def top(self):
        """Returns the top element of the stack without removing it."""
        if self.is_empty():
            return None
        return self.data[self.size]

    def size(self):
        """Returns the number of elements in the stack."""
        return self.size

    def is_empty(self):
        """Returns whether the stack is empty."""
        return self.size == 0


if __name__ == '__main__':
    a_stack = ArrayStack()
    print(a_stack)
    a_stack.push(1)
    print(a_stack)
    a_stack.push(2)
    print(a_stack)
    a_stack.push(3)
    print(a_stack)
    a_stack.push(4)
    print(a_stack)
    a_stack.pop()
    print(a_stack)
