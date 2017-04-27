"""A heap is a specialised tree-based data structure that satisfies the heap property."""

from abc import ABC, abstractmethod


class Heap(ABC):
    @abstractmethod
    def __init__(self, *args):
        for arg in args:
            self.insert(arg)

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def min(self):
        pass

    @abstractmethod
    def remove_min(self):
        pass


class BinaryHeap(Heap):
    """A binary heap is priority queue that uses a binary tree.
    Space: O(n)
    Search: O(n)
    Insert: O(log n)
    Delete: O(log n)
    Peek: O(1)
    """
    def __init__(self, *args):
        self.size = 0
        self.data = []
        super().__init__(*args)

    def __repr__(self):
        result = ', '.join(str(x) for x in self.data)
        return 'BinaryHeap<{}>'.format(result)

    def empty(self):
        pass

    def insert(self):
        pass

    def min(self):
        pass

    def remove_min(self):
        pass

    def _upheap(self):
        pass


if __name__ == '__main__':
    heap = Heap()
    print(heap)
