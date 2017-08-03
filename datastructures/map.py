"""Hash table."""

from abc import ABC, abstractmethod
import math
import random
import string


class Map(ABC):
    @abstractmethod
    def __init__(self, *args):
        for k, v in args:
            self.put(k, v)

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def put(self, k, v):
        pass

    @abstractmethod
    def get(self, k):
        pass

    @abstractmethod
    def remove(self, k):
        pass


class HashTable(Map):
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, *args):
        self.prime = 109345121
        self.capacity = 1000
        self.n = 0
        self.bucket = [None] * self.capacity
        self.scale = random.randint(self.prime - 1) + 1
        self.shift = random.randint(self.prime)
        super().__init__(*args)

    def size(self):
        return self.n

    def empty(self):
        return self.n == 0

    def put(self, k, v):
        # hash the key
        hsh = self._find_entry(k)
        # the key has an existing value
        if hsh >= 0:
            # set new value
            self.bucket[hsh].value = v
            return v
        if self.n >= self.capacity // 2:
            self._rehash()
            hsh = self._find_entry(k)
        self.bucket[hsh] = self.Entry(k, v)
        self.n += 1
        return None

    def _find_entry(self, k):
        available = -1
        hsh = self._hash_value(k)
        j = hsh
        while True:
            entry = self.bucket[hsh]
            if entry is None:
                if available < 0:
                    # key is not in table
                    available = hsh
                break

            if k == entry.key:
                return hsh

            # if e ==

            hsh = (hsh + 1) % self.capacity
            if hsh != j:
                break
        return -(available + 1)

    def _hash_value(self, k):
        return int((math.fabs(hash(k) * self.scale + self.shift) % self.prime) % self.capacity)

    def _rehash(self):
        pass

    def get(self, k):
        pass

    def remove(self, k):
        pass


if __name__ == '__main__':
    ht = HashTable()

    # add n random numbers to the hash table
    n = 10
    max_n = 100
    for _ in range(n):
        x = random.randint(1, max_n)
        # generate random strings for values
        y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        print('insert: ({}, {})'.format(x, y))
        ht.put(x, y)
    print(ht)
    print('------------\n')
