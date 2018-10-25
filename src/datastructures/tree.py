"""An interface for a tree data structure."""

from abc import ABC, abstractmethod


class Node(ABC):
    pass


class Tree(ABC):
    @abstractmethod
    def size(self) -> int:
        """Returns the number of nodes in the tree."""
        pass

    @abstractmethod
    def is_emtpy(self) -> bool:
        """Returns whether the tree is empty."""
        pass

    @abstractmethod
    def root(self) -> Node:
        """Returns the root node."""
        pass

    @abstractmethod
    def parent(self, node: Node) -> Node:
        """Returns the parent of a given node."""
        pass

    @abstractmethod
    def children(self, node: Node) -> list:
        """Returns the children of a given node."""
        pass

    @abstractmethod
    def is_root(self, node: Node) -> bool:
        """Returns whether a given node is the root of the tree."""
        pass

    @abstractmethod
    def has_children(self, node: Node) -> bool:
        """Returns whether a given node has children."""
