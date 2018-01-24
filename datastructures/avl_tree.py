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
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        self.height = 1 + max(left_height, right_height)
        self.balance = left_height - right_height

    def __bool__(self):
        return self.key is not None


class AVLTree(BinaryTree, Dictionary):
    def __init__(self, *args):
        self.size: int = 0
        self.height: int = 0
        self.root: AVLNode = None
        super().__init__(*args)

    def size(self) -> int:
        """Returns the number of nodes in the tree."""
        return self.size

    def is_emtpy(self) -> bool:
        """Returns whether the tree is empty."""
        return self.size == 0

    def insert(self, key, value=None) -> AVLNode:
        """Insert an entry into the AVL tree."""
        if self.root is None:
            self.size += 1
            self.height += 1
            self.root = AVLNode(key, value, None)
            return self.root
        else:
            node = self._insert(key, value, self.root)
            parent = self.parent(node)
            self._rebalance(parent)
            return node

    def _insert(self, key, value, node: AVLNode) -> AVLNode:
        if key < node.key:
            if node.has_left():
                return self._insert(key, value, node.left)
            else:
                self.size += 1
                node.left = AVLNode(key, value, node)
                return node.left
        else:
            if node.has_right():
                return self._insert(key, value, node.right)
            else:
                self.size += 1
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
            self.root = pivot
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
            self.root = pivot
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
        return self.root

    def parent(self, node: AVLNode) -> AVLNode:
        """Returns the parent of a given node."""
        return node.parent

    def children(self, node: AVLNode) -> list:
        """Returns the children of a given node."""
        pass

    def is_root(self, node: AVLNode) -> bool:
        """Returns whether a given node is the root of the tree."""
        return node == self.root

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

    # def preorder_print(self, node: AVLNode, result: list, n: int) -> list:
    #     if node is None:
    #         return result
    #
    #     level = []
    #     if node.has_left():
    #         level.append(str(node.left))
    #     else:
    #         level.append(None)
    #     if node.has_right():
    #         level.append(str(node.right))
    #     else:
    #         level.append(None)
    #
    #     if len(result) >= n:
    #         result.append([])
    #     result[n] = result[n] + level
    #
    #     self.preorder_print(node.left, result, n + 1)
    #     self.preorder_print(node.right, result, n + 1)
    #     return result

    # def old(self):
    #     result = '[AVLTree:{}]'.format(self.size)
    #     if self.is_emtpy():
    #         return result + ' - Empty'
    #     else:
    #         # convert tree to a list representation for printing
    #         root = self.root
    #         levels = self.preorder_print(root, [[root]], 1)
    #         levels = [x for x in levels if x]  # remove empty lists
    #         # print list representation
    #         height = len(levels)
    #         space = '  '
    #         for i, level in enumerate(levels):
    #             level_str = ''
    #             m = height - (i + 1)
    #             offset = space * m
    #             level_str += offset + ' '
    #             spaces = space * (i + 1)
    #             spaces_i = space * m
    #             # row of nodes
    #             for j, node in enumerate(level):
    #                 level_str += '{}{}'.format(str(node), spaces)
    #             # row of lines
    #             level_str += '\n' + offset
    #             for _ in level:
    #                 level_str += '/{}\\{}'.format(spaces_i, space)
    #             result += '\n' + level_str
    #     return result

    # def __str__(self):
    #     if self.is_emtpy():
    #         return 'Empty'
    #     else:
    #         result =

    # def print(self):
    #     stack = []
    #     node = self.root
    #     self._print(node, stack)
    #
    # def _print(self, node: AVLNode, stack):
    #     print(str(node))
    #     if node.value is not None:
    #         print('{} `--'.format())

    def __str__(self):
        queue, out = [self.root], []
        while queue:
            out.append('{}'.format([str(node) for node in queue]))
            if any(node for node in queue):
                children = []
                for node in queue:
                    for subnode in (node.left, node.right):
                        children.append(subnode if subnode else AVLNode(None))
                queue = children
            else:
                break
        return '\n'.join(out)


if __name__ == '__main__':
    import string
    import random

    tree = AVLTree()

    tree.insert(16)
    tree.insert(13)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(10)
    tree.insert(11)
    tree.insert(15)
    tree.insert(14)
    tree.insert(1)

    # tree.insert(4)
    # tree.insert(5)
    # tree.insert(8)
    # tree.insert(11)
    # tree.insert(12)
    # tree.insert(17)
    # tree.insert(18)

    # tree.insert(22)
    # tree.insert(10)
    # tree.insert(20)
    # tree.insert(12)
    # tree.insert(25)
    # tree.insert(28)
    # tree.insert(30)
    # tree.insert(36)
    # tree.insert(38)
    # tree.insert(40)
    # tree.insert(48)

    # tree.insert(25)
    # tree.insert(15)
    # tree.insert(50)
    # tree.insert(10)
    # tree.insert(22)
    # tree.insert(35)
    # tree.insert(70)

    # add n random entries into the AVL tree
    # n = 10
    # max_n = 100
    # for _ in range(n):
    #     x = random.randint(1, max_n)
    #     y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    #     print('insert: ({}, {})'.format(x, y))
    #     tree.insert(x, y)
    # print('------------\n')
    print(tree)
