"""Priority Queues."""

from abc import ABC, abstractmethod

from src.datastructures.heap import BinaryHeap


class PriorityQueue(ABC):
    @abstractmethod
    def __init__(self, *args):
        for arg in args:
            self.enqueue(arg)

    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in the priority queue."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns whether the priority queue is empty."""
        pass

    @abstractmethod
    def enqueue(self, k, v):
        """Enqueue an entry in the priority queue."""
        pass

    @abstractmethod
    def dequeue(self):
        """Dequeue an entry from the priority queue."""
        pass


class HeapPriorityQueue(PriorityQueue):
    """A priority queue implementation using a heap data structure."""
    def __init__(self, *args):
        self.heap = BinaryHeap()
        super().__init__(*args)

    def __repr__(self):
        return self.heap.__repr__()

    def size(self) -> int:
        """Returns the number of elements in the priority queue."""
        return self.heap.size

    def is_empty(self) -> bool:
        """Returns whether the priority queue is empty."""
        return self.heap.is_empty()

    def enqueue(self, k, v):
        """Enqueue an entry in the priority queue."""
        self.heap.insert((k, v))

    def dequeue(self):
        """Dequeue an entry from the priority queue."""
        if self.is_empty():
            return None
        else:
            return self.heap.remove_min()


if __name__ == '__main__':
    import string
    import random

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
