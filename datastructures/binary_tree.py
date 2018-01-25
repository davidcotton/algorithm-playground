"""Binary Tree interface."""

from tree import Tree, Node
from abc import abstractmethod


class BinaryNode(Node):
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent: BinaryNode = parent
        self.left: BinaryNode = None
        self.right: BinaryNode = None

    def has_left(self) -> bool:
        return self.left is not None

    def has_right(self) -> bool:
        return self.right is not None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __repr__(self):
        value = self.key if self.key is not None else '..'
        return '<{}>'.format(value)


class BinaryTree(Tree):
    @abstractmethod
    def left(self, node: BinaryNode) -> BinaryNode:
        """Returns the left child of a node."""
        pass

    @abstractmethod
    def right(self, node: BinaryNode) -> BinaryNode:
        """Returns the right child of a node."""
        pass

    @abstractmethod
    def has_left(self, node: BinaryNode) -> bool:
        """Returns whether a node has a left child."""
        pass

    @abstractmethod
    def has_right(self, node: BinaryNode) -> bool:
        """Returns whether a node has a right child."""
        pass
