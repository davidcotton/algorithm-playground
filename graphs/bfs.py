from collections import deque
from graphs.graph import Vertex
from typing import List, Optional


def bfs_search(start: Vertex, goal: Vertex) -> Optional[List[Vertex]]:
    """Search for the goal vertex within a graph.
    Graph must have no loops and no edge weights to work.
    Returns the path as a list of vertices if goal is found else None."""
    frontier: deque[Vertex] = deque([start])
    paths: deque[List] = deque([[]])
    while frontier:
        vertex = frontier.popleft()
        path = paths.popleft()
        path.append(vertex.key())
        if vertex is goal:
            return path
        for neighbour in vertex.neighbours():
            frontier.append(neighbour)
            paths.append(path[:])
    return None


def bfs(root: Vertex) -> List[List]:
    """Search a graph via Breadth-First-Search from a vertex.
    Returns a tree describing every vertex that is reachable from the source vertex.
    """
    frontier: deque[Vertex] = deque([root])
    paths: deque[List] = deque([[]])
    while frontier:
        vertex = frontier.popleft()
        path = paths.popleft()
        path.append(vertex.key())
        if vertex.neighbours():
            for neighbour in vertex.neighbours():
                frontier.append(neighbour)
                paths.append(path[:])
        else:
            paths.append(path)
    return list(paths)