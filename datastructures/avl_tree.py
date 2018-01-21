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


class AVLNode(BinaryNode):
    def __init__(self, value, parent):
        super(AVLNode, self).__init__(value, parent)
        self.height = 0
        self.left: AVLNode = None
        self.right: AVLNode = None
        if self.left is not None:
            self.height = max(self.height, 1 + self.left.height)
        if self.right is not None:
            self.height = max(self.height, 1 + self.right.height)

    def get_height(self):
        return self.height

    def set_height(self):
        left = self.left.height if self.left is not None else 0
        right = self.right.height if self.right is not None else 0
        self.height = 1 + max(left, right)


class AVLTree(BinaryTree):
    def __init__(self, *args):
        self.size: int = 0
        self.height: int = 0
        self.root: AVLNode = None
        for arg in args:
            self.insert(arg)

    def size(self) -> int:
        """Returns the number of nodes in the tree."""
        return self.size

    def is_emtpy(self) -> bool:
        """Returns whether the tree is empty."""
        return self.size == 0

    def insert(self, value) -> AVLNode:
        """Insert an entry into the AVL tree."""
        if self.root is None:
            self.size += 1
            self.height += 1
            self.root = AVLNode(value, None)
            return self.root
        else:
            node = self._insert(value, self.root)
            parent = self.parent(node)
            self._rebalance(parent)
            return node

    def _insert(self, value, node: AVLNode) -> AVLNode:
        if value < node.value:
            if node.has_left():
                return self._insert(value, node.left)
            else:
                self.size += 1
                node.left = AVLNode(value, node)
                return node.left
        else:
            if node.has_right():
                return self._insert(value, node.right)
            else:
                self.size += 1
                node.right = AVLNode(value, node)
                return node.right

    def _rebalance(self, node: AVLNode):
        # traverse up the tree
        while not self.is_root(node):
            node = self.parent(node)
            node.set_height()
            if not self._is_balanced(node):
                other = ''

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

    def preorder_print(self, node: AVLNode, result: list, n: int) -> list:
        if node is None:
            return result

        level = []
        if node.has_left():
            level.append(str(node.left))
        else:
            level.append(None)
        if node.has_right():
            level.append(str(node.right))
        else:
            level.append(None)

        if len(result) >= n:
            result.append([])
        result[n] = result[n] + level

        self.preorder_print(node.left, result, n + 1)
        self.preorder_print(node.right, result, n + 1)
        return result

    def old(self):
        result = '[AVLTree:{}]'.format(self.size)
        if self.is_emtpy():
            return result + ' - Empty'
        else:
            # convert tree to a list representation for printing
            root = self.root
            levels = self.preorder_print(root, [[root]], 1)
            levels = [x for x in levels if x]  # remove empty lists
            # print list representation
            height = len(levels)
            space = '  '
            for i, level in enumerate(levels):
                level_str = ''
                m = height - (i + 1)
                offset = space * m
                level_str += offset + ' '
                spaces = space * (i + 1)
                spaces_i = space * m
                # row of nodes
                for j, node in enumerate(level):
                    level_str += '{}{}'.format(str(node), spaces)
                # row of lines
                level_str += '\n' + offset
                for _ in level:
                    level_str += '/{}\\{}'.format(spaces_i, space)
                result += '\n' + level_str
        return result

    # def __str__(self):
    #     if self.is_emtpy():
    #         return 'Empty'
    #     else:
    #         result =

    def print(self):
        stack = []
        node = self.root
        self._print(node, stack)

    def _print(self, node: AVLNode, stack):
        print(str(node))
        if node.value is not None:
            print('{} `--'.format())



if __name__ == '__main__':
    import string
    import random

    tree = AVLTree()

    tree.insert(22)
    tree.insert(10)
    tree.insert(20)
    tree.insert(12)
    tree.insert(25)
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
    # print(tree)
    tree.print(tree.root)

    # # add n random entries into the AVL tree
    # n = 10
    # max_n = 100
    # for _ in range(n):
    #     x = random.randint(1, max_n)
    #     y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    #     print('insert: ({}, {})'.format(x, y))
    #     tree.insert(x, y)
    # print('------------\n')
    # print(tree)
