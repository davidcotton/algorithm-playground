"""Priority Queues."""

from abc import ABC, abstractmethod
from heap import BinaryHeap
import string
import random


class PriorityQueue(ABC):
    @abstractmethod
    def __init__(self, *args):
        for arg in args:
            self.enqueue(arg)

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def enqueue(self, k, v):
        pass

    @abstractmethod
    def dequeue(self):
        pass


class HeapPriorityQueue(PriorityQueue):
    """A priority queue implementation using a heap data structure."""
    def __init__(self, *args):
        self.heap = BinaryHeap()
        super().__init__(*args)

    def __repr__(self):
        return self.heap.__repr__()

    def size(self):
        return self.heap.size

    def empty(self):
        return self.heap.empty()

    def enqueue(self, k, v):
        self.heap.insert((k, v))

    def dequeue(self):
        if self.empty():
            return None
        else:
            return self.heap.remove_min()


if __name__ == '__main__':
    pq = HeapPriorityQueue()

    # add n random numbers to the priority queue
    n = 10
    max_n = 100
    for _ in range(n):
        x = random.randint(1, max_n)
        # generate random strings as values to make it easier to differentiate the priorities
        y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        print('enqueue: ({}, {})'.format(x, y))
        pq.enqueue(x, y)
    print(pq)
    print('------------\n')

    # remove the n smallest numbers from the priority queue
    n = 5
    for _ in range(n):
        print('dequeue: {}'.format(pq.dequeue()))
        print(pq)
        print()
