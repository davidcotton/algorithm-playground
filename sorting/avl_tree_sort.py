"""Use an AVL Tree to sort."""

from avl_tree import AVLTree


class AVLTreeSort:
    def sort(self, l):
        AVLTree(*l)


if __name__ == '__main__':
    # print(AVLTreeSort().sort([4, 2, 8, 6, 0, 5, 1, 7, 3, 9]))

    avl_tree = AVLTree(*[4, 2, 8, 6, 0, 5, 1, 7, 3, 9])
    print(avl_tree)
