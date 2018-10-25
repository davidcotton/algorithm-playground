"""Graph representation in which each vertex stores a collection of adjacent vertices in a list data structure."""

from typing import Dict, List

from src.graphs.graph import Edge, Graph, Vertex


class AdjacencyListVertex(Vertex):
    def __init__(self, key, neighbours: List=None) -> None:
        super().__init__(key)
        self._neighbours: List[Vertex] = neighbours if neighbours is not None else []


class AdjacencyListGraph(Graph):
    """An array backed implementation of an Adjacency List Graph."""
    def __init__(self, adjacency_list=None) -> None:
        self._vertices = []
        if adjacency_list is not None:
            for vertices in adjacency_list:
                self.add_vertex(vertices)

    def vertices(self) -> List[Vertex]:
        """Get all vertices."""
        vertices: Dict[int, Vertex] = {}
        for i, neighbours in enumerate(self._vertices):
            if i in vertices:
                vertex = vertices[i]
            else:
                vertex = AdjacencyListVertex(i)
                vertices[i] = vertex

            for n in neighbours:
                if n in vertices:
                    neighbour = vertices[n]
                else:
                    neighbour = AdjacencyListVertex(n)
                    vertices[n] = neighbour
                vertex.add_neighbour(neighbour)
        return list(vertices.values())

    def edges(self) -> List[Edge]:
        """Get all edges."""
        # @todo: implement
        raise NotImplementedError

    def add_vertex(self, v: Vertex) -> None:
        """Insert a vertex v."""
        self._vertices.append(v)

    def remove_vertex(self, vertex: Vertex) -> None:
        """Remove a vertex v and its incident edges."""
        for v in self._vertices:
            if vertex == v:
                self._vertices.remove(vertex)

    def are_adjacent(self, v: Vertex, w: Vertex) -> bool:
        """True if v and w are adjacent."""
        # @todo: implement
        raise NotImplementedError

    def add_edge(self, e: Edge, v: Vertex, w: Vertex) -> None:
        """Insert an edge between two vertices."""
        # @todo: implement
        raise NotImplementedError

    def remove_edge(self, e: Edge) -> None:
        """Remove an edge."""
        # @todo: implement
        raise NotImplementedError


def get_graph():
    """Get a simple adjacency list graph."""
    graph = AdjacencyListGraph([[1, 2], [2, 3], [4], [4, 5], [5], []])
    return graph


def generate_graph(n):
    """Generate a random graph."""
    # @todo: implement
    graph = AdjacencyListGraph()

    return graph
