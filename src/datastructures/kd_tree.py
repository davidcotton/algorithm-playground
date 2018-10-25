"""Kd Tree."""

import math
import pprint

from src.datastructures.tree import Tree, Node


class KdNode(Node):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class KdTree(Tree):
    def __init__(self, dimensions=2):
        self._k: int = dimensions
        self._size: int = 0
        self._height: int = 0
        self._root: KdNode = None

    def size(self) -> int:
        """Returns the number of nodes in the tree."""
        return self._size

    def is_emtpy(self) -> bool:
        """Returns whether the tree is empty."""
        return self._size == 0

    def root(self) -> Node:
        """Returns the root node."""
        return self._root

    def parent(self, node: Node) -> Node:
        pass

    def children(self, node: Node) -> list:
        pass

    def is_root(self, node: Node) -> bool:
        """Returns whether a given node is the root of the tree."""
        return node == self._root

    def has_children(self, node: Node) -> bool:
        pass

    def insert(self):
        pass

    def distance(self, point_1, point_2):
        x1, y1 = point_1
        x2, y2 = point_2

        dx = x1 - x2
        dy = y1 - y2

        return math.sqrt(dx * dx + dy * dy)

    def closest_point(self, points, new_point):
        best_point = None
        best_distance = None

        for current_point in points:
            current_distance = self.distance(new_point, current_point)
            if best_distance is None or current_distance < best_distance:
                best_distance = current_distance
                best_point = current_point

        return best_point

    def build_kdtree(self, points, depth=0):
        n = len(points)
        if n <= 0:
            return None

        axis = depth % k
        split_point = n // 2

        sorted_points = sorted(points, key=lambda point: point[axis])

        return {
            'point': sorted_points[split_point],
            'left': self.build_kdtree(sorted_points[:split_point], depth + 1),
            'right': self.build_kdtree(sorted_points[split_point + 1:], depth + 1)
        }

    def kdtree_naive_closest_point(root, point, depth=0, best=None):
        if root is None:
            return best

        axis = depth % k

        next_best = None
        next_branch = None

        if dis


if __name__ == '__main__':
    tree = KdTree()
    nodes = [(4, 14), (6, 21), (8, 2), (11, 13), (15, 20), (18, 3), (21, 11)]
    tree = build_kdtree(nodes)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tree)
    derp = 1
