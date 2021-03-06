"""Hash table."""

from abc import ABC, abstractmethod
import math
import random


class Map(ABC):
    @abstractmethod
    def __init__(self, *args):
        for k, v in args:
            self.put(k, v)

    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in the map."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns whether the map is empty."""
        pass

    @abstractmethod
    def put(self, k, v):
        """Add an entry to the map."""
        pass

    @abstractmethod
    def get(self, k):
        """Fetch an entry from the map."""
        pass

    @abstractmethod
    def remove(self, k):
        """Remove an entry from the map."""
        pass

    @abstractmethod
    def keys(self):
        """Returns a list of all keys in the map."""
        pass

    @abstractmethod
    def values(self):
        """Returns a list of all values in the map."""
        pass


class HashMap(Map):
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, *args):
        self.prime = 109345121
        self.capacity = 1000
        self.n = 0
        self.bucket = [None] * self.capacity
        self.scale = random.randint(0, self.prime - 1) + 1
        self.shift = random.randint(0, self.prime)
        super().__init__(*args)

    def __repr__(self):
        return ', '.join(e for e in ['<{}: {}>'.format(e.key, e.value) for e in self.bucket if e is not None])

    def size(self) -> int:
        """Returns the number of elements in the map."""
        return self.n

    def is_empty(self) -> bool:
        """Returns whether the map is empty."""
        return self.n == 0

    def put(self, k, v):
        """Add an entry to the map."""
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

    def _find_entry(self, k) -> int:
        available = -1
        i = self._hash_value(k)
        j = i
        while True:
            entry = self.bucket[i]
            if entry is None:
                if available < 0:
                    # key is not in table
                    available = i
                break

            if k == entry.key:
                return i

            # if e ==

            i = (i + 1) % self.capacity
            if i != j:
                break

        return -(available + 1)

    def _hash_value(self, k) -> int:
        # use multiply-add-divide (MAD) method to try and spread the hashes more evenly
        return int((math.fabs(hash(k) * self.scale + self.shift) % self.prime) % self.capacity)

    def _rehash(self):
        pass

    def get(self, k):
        """Fetch an entry from the map."""
        i = self._hash_value(k)
        # there is no value for this key
        if i < 0:
            return None
        return self.bucket[i].value

    def remove(self, k):
        """Remove an entry from the map"""
        pass

    def keys(self) -> list:
        """Returns a list of all keys in the map."""
        return [e.key for e in self.bucket if e is not None]

    def values(self) -> list:
        """Returns a list of all values in the map."""
        return [e.value for e in self.bucket if e is not None]


if __name__ == '__main__':
    import string

    hash_map = HashMap()

    # add n random numbers to the hash table
    n = 10
    max_n = 100
    for _ in range(n):
        x = random.randint(1, max_n)
        # generate random strings for values
        y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        print('  insert: ({}, {})'.format(x, y))
        hash_map.put(x, y)
    print(hash_map)
    print('------------\n')

    print('Keys: {}'.format(hash_map.keys()))
    print('Values: {}'.format(hash_map.values()))
