"""Depth-First Search
Search a graph by following one path at a time."""

from typing import List, Optional

from src.graphs.adjacencylist import get_graph
from src.graphs.graph import Graph, Vertex


def dfs_search(start: Vertex, goal: Vertex) -> Optional[List[Vertex]]:
    """Search for the goal vertex within a graph in a depth-first manner."""
    pass


def dfs(root: Vertex) -> List[Vertex]:
    pass


def dfs_old(adj, vertices):
    parent = {}
    for s in vertices:
        if s not in parent:
            parent[s] = dfs_visit_old(adj, s)
    return parent


def dfs_visit_old(adj, s):
    """Depth-first Search.
    Returns a tree describing every vertex that is reachable from the source vertex.

        Args:
            adj: The adjacency list to search
            s: The source vertex

        Returns: {}
        """
    parent = {s: None}
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs(adj, v)
    return parent


if __name__ == '__main__':
    graph: Graph = get_graph()
    vertices: List[Vertex] = graph.vertices()

    shortest_path = dfs_search(vertices[0], vertices[4])
    print('shortest path', shortest_path)

    all_paths = dfs(vertices[0])
    print('all paths', all_paths)
