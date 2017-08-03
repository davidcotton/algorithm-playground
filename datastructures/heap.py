"""A heap is a specialised tree-based data structure that satisfies the heap property."""

from abc import ABC, abstractmethod
from random import randint


class Heap(ABC):
    @abstractmethod
    def __init__(self, *args):
        for arg in args:
            self.insert(arg)

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def insert(self, k):
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
        self.data = [0]
        super().__init__(*args)

    def __repr__(self):
        return 'BinaryHeap<{}>'.format(', '.join(str(x) for x in self.data))

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def insert(self, k):
        self.data.append(k)
        self.size += 1
        self._upheap(self.size)

    def min(self):
        if self.empty():
            return None
        else:
            return self.data[1]

    def remove_min(self):
        min_val = self.data[1]
        self.data[1] = self.data[self.size]
        self.size -= 1
        self.data.pop()
        self._downheap(1)
        return min_val

    def _upheap(self, i):
        while i // 2 > 0:
            if self.data[i] < self.data[i // 2]:
                tmp = self.data[i // 2]
                self.data[i // 2] = self.data[i]
                self.data[i] = tmp
            i //= 2

    def _downheap(self, i):
        while (i * 2) <= self.size:
            min_child = self._min_child(i)
            if self.data[i] > self.data[min_child]:
                self.data[i], self.data[min_child] = self.data[min_child], self.data[i]
            else:
                break
            i = min_child

    def _min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.data[i * 2] < self.data[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


if __name__ == '__main__':
    heap = BinaryHeap()

    # add n random numbers to the heap
    n = 10
    max_n = 100
    for _ in range(n):
        x = randint(1, max_n)
        print('Adding: {}'.format(x))
        heap.insert(x)
    print(heap)
    print('------------\n')

    # remove the n smallest numbers from the heap
    n = 5
    for _ in range(n):
        print('remove_min: {}'.format(heap.remove_min()))
        print(heap)
        print()
