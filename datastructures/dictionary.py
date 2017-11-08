"""An interface for a dictionary data structure that stores key-value pairs."""

from abc import ABC, abstractmethod


class Dictionary(ABC):
    @abstractmethod
    def __init__(self, *args):
        for arg in args:
            self.insert(arg)

    @abstractmethod
    def size(self) -> int:
        """Returns the number of entries in a dictionary."""
        pass

    @abstractmethod
    def is_emtpy(self) -> bool:
        """Returns whether the dictionary is empty."""
        pass

    @abstractmethod
    def insert(self, key, value):
        """Insert an item into the dictionary. Return the created entry."""
        pass

    @abstractmethod
    def remove(self, entry):
        """Remove and return a given entry from a dictionary."""
        pass
