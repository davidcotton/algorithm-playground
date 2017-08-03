"""
    Binary tree.
"""


class BinaryTree:
    def __init__(self):
        self.root = None

    def root(self):
        return self.root

    def add(self, val):
        """Add a value to a binary tree."""
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.has_left():
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.has_right():
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def __repr__(self):
        result = ''
        levels = []
        # while

        return result


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __repr__(self):
        return 'Node<{}>'.format(self.val)


if __name__ == '__main__':
    bt = BinaryTree()
    # print(bt)
    bt.add(3)
    # print(bt)
    bt.add(2)
    # print(bt)
    bt.add(4)
    # print(bt)
    bt.add(1)
    # print(bt)
    # bt.pop()
    print(bt)
    derp = 1
