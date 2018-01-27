"""AVL self-balancing binary search tree.
An AVL tree is a binary search tree that implements the balanced property.
The heights of any two subtrees in an AVL tree must differ by at most 1.
If they differ by more than 1 the tree must be rebalanced.

Operation | Average  | Worst Case
--------------------------------
Space     | O(n)     | O(n)
Search    | O(log n) | O(log n)
Insert    | O(log n) | O(log n)
Delete    | O(log n) | O(log n)
"""

from binary_tree import BinaryTree, BinaryNode
from dictionary import Dictionary


class AVLNode(BinaryNode):
    def __init__(self, key, value=None, parent=None):
        super(AVLNode, self).__init__(key, value, parent)
        self.height: int = 0
        self.balance: int = 0
        self.parent: AVLNode = parent
        self.left: AVLNode = None
        self.right: AVLNode = None
        if self.left is not None:
            self.height = max(self.height, 1 + self.left.height)
        if self.right is not None:
            self.height = max(self.height, 1 + self.right.height)

    def get_height(self):
        return self.height

    def update_height(self):
        left_height = self.left.height + 1 if self.left is not None else 0
        right_height = self.right.height + 1 if self.right is not None else 0
        self.height = max(left_height, right_height)
        self.balance = left_height - right_height

    def __bool__(self):
        return self.key is not None


class AVLTree(BinaryTree, Dictionary):
    def __init__(self, *args):
        self._size: int = 0
        self._height: int = 0
        self._root: AVLNode = None
        super().__init__(*args)

    def size(self) -> int:
        """Returns the number of nodes in the tree."""
        return self._size

    def is_emtpy(self) -> bool:
        """Returns whether the tree is empty."""
        return self._size == 0

    def insert(self, key, value=None) -> AVLNode:
        """Insert an entry into the AVL tree."""
        if self._root is None:
            self._size += 1
            self._height += 1
            self._root = AVLNode(key, value, None)
            return self._root
        else:
            node = self._insert(key, value, self._root)
            parent = self.parent(node)
            self._rebalance(parent)
            return node

    def _insert(self, key, value, node: AVLNode) -> AVLNode:
        if key < node.key:
            if node.has_left():
                return self._insert(key, value, node.left)
            else:
                self._size += 1
                node.left = AVLNode(key, value, node)
                return node.left
        else:
            if node.has_right():
                return self._insert(key, value, node.right)
            else:
                self._size += 1
                node.right = AVLNode(key, value, node)
                return node.right

    def _rebalance(self, node: AVLNode):
        # # traverse up the tree
        # while not self.is_root(node):
        #     node = self.parent(node)
        #     node.update_height()
        #     if not self._is_balanced(node):
        #         other = ''
        node.update_height()
        if node.balance == 2:
            if node.left.balance != -1:
                # left-left case
                self._rotate_right(node)
                if node.parent.parent is not None:
                    self._rebalance(node.parent.parent)
            else:
                # left-right case
                self._rotate_left(node.left)
                self._rebalance(node)
        elif node.balance == -2:
            if node.right.balance != 1:
                # right-right case
                self._rotate_left(node)
                if node.parent.parent is not None:
                    self._rebalance(node.parent.parent)
            else:
                # right-left case
                self._rotate_right(node.right)
                self._rebalance(node)
        else:
            if node.parent is not None:
                self._rebalance(node.parent)

    def _rotate_left(self, node: AVLNode):
        if node.parent is None:
            is_left = node.parent
        else:
            is_left = node is node.parent.left

        pivot = node.right
        if pivot is None:
            return
        node.right = pivot.left
        if pivot.left is not None:
            node.right.parent = node
        pivot.left = node
        pivot.parent = node.parent
        node.parent = pivot

        if is_left is None:
            self._root = pivot
        elif is_left:
            pivot.parent.left = pivot
        else:
            pivot.parent.right = pivot

        node.update_height()
        pivot.update_height()

    def _rotate_right(self, node: AVLNode):
        if node.parent is None:
            is_left = node.parent
        else:
            is_left = node is node.parent.left

        pivot = node.left
        if pivot is None:
            return
        node.left = pivot.right
        if pivot.right is not None:
            node.left.parent = node
        pivot.right = node
        pivot.parent = node.parent
        node.parent = pivot

        if is_left is None:
            self._root = pivot
        elif is_left:
            pivot.parent.left = pivot
        else:
            pivot.parent.right = pivot

        node.update_height()
        pivot.update_height()

    @staticmethod
    def _is_balanced(node: AVLNode) -> bool:
        """Returns whether a node is balanced.
        A tree is balanced if it has a maximum balance factor of 1."""
        left = node.left.height if node.left is not None else 0
        right = node.right.height if node.right is not None else 0
        bf = left - right
        return -1 <= bf <= 1

    def remove(self, entry) -> AVLNode:
        """Remove an entry from the AVL tree."""
        pass

    def root(self) -> AVLNode:
        """Returns the root node."""
        return self._root

    def parent(self, node: AVLNode) -> AVLNode:
        """Returns the parent of a given node."""
        return node.parent

    def children(self, node: AVLNode) -> list:
        """Returns the children of a given node."""
        pass

    def is_root(self, node: AVLNode) -> bool:
        """Returns whether a given node is the root of the tree."""
        return node == self._root

    def left(self, node: AVLNode) -> AVLNode:
        """Returns the left child of a node."""
        return node.left

    def right(self, node: AVLNode) -> AVLNode:
        """Returns the right child of a node."""
        return node.right

    def has_left(self, node: AVLNode) -> bool:
        """Returns whether a node has a left child."""
        return node.left is not None

    def has_right(self, node: AVLNode) -> bool:
        """Returns whether a node has a right child."""
        return node.right is not None

    def has_children(self, node: AVLNode) -> bool:
        """Returns whether a given node has children."""
        return self.has_left(node) and self.has_right(node)

    def __str__(self):
        queue, out, temp = [self._root], [], []
        while queue and any(node for node in queue):
            out.append(' '.join([str(node) for node in queue]))
            for node in queue:
                for subnode in (node.left, node.right):
                    temp.append(subnode if subnode else AVLNode(None))
            queue, temp = temp, []
        return '\n'.join(out)


if __name__ == '__main__':
    # a couple of test trees
    # tree = AVLTree(37, 14, 13)
    # tree = AVLTree(16, 13, 4, 5, 6, 10, 11, 15, 14, 1)
    # tree = AVLTree(4, 5, 8, 11, 12, 17, 18)
    # tree = AVLTree(22, 10, 20, 12, 25, 28, 30, 36, 38, 40, 48)
    # tree = AVLTree(25, 15, 50, 10, 22, 35, 70)

    # or a random tree
    import string
    import random

    tree = AVLTree()
    n = 3
    max_n = 100
    for _ in range(n):
        x = random.randint(1, max_n)
        y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        print('insert: ({}, {})'.format(x, y))
        tree.insert(x, y)
    print('------------\n')

    print(tree, '\n')
    print('Tree size: {}'.format(tree.size()))
