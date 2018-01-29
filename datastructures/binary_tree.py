"""Binary Tree interface."""

from tree import Tree, Node
from abc import abstractmethod


class BinaryNode(Node):
    def __init__(self, key, value=None, parent=None):
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
        return '<{}>'.format(str(self.key).zfill(2) if self.key is not None else '..')

    def __bool__(self):
        return self.key is not None


class BinaryTree(Tree):
    def __init__(self):
        self._root: BinaryNode = None

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

    def __str__(self):
        queue, out, temp = [self._root], [], []
        while queue and any(node for node in queue):
            out.append(' '.join([str(node) for node in queue]))
            for node in queue:
                for subnode in (node.left, node.right):
                    temp.append(subnode if subnode else BinaryNode(None))
            queue, temp = temp, []
        return '\n'.join(out)

    def pretty_print(self):
        queue, levels, temp = [self._root], [], []
        while queue and any(node for node in queue):
            levels.append([str(node) for node in queue])
            for node in queue:
                for subnode in (node.left, node.right):
                    temp.append(subnode if subnode else BinaryNode(None))
            queue, temp = temp, []
        height = len(levels)
        width = 2 ** (height - 1)
        output = ''
        for i, level in enumerate(levels):
            spaces = '    ' * (2 ** (height - i) - 1)
            line = spaces.join(level)
            output += line.center(width * 8) + '\n'
        return output
