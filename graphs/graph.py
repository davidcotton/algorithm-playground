from abc import ABC, abstractmethod
from typing import Dict, List, Set


class Vertex:
    """A graph vertex."""
    def __init__(self, key: str) -> None:
        super().__init__()
        self._key: str = str(key)
        self._neighbours: List[Vertex] = []

    def key(self) -> str:
        return self._key

    def neighbours(self) -> list:
        return self._neighbours

    def add_neighbour(self, v) -> None:
        self._neighbours.append(v)

    def __repr__(self) -> str:
        return f'<{self.key()}>'


class Edge:
    """A graph edge."""
    def __init__(self, v: Vertex, w: Vertex, value=None) -> None:
        super().__init__()
        self.vertices = (v, w)
        self.value = value

    def __repr__(self) -> str:
        return f'<{self.vertices[0]}-{self.vertices[1]} ({self.value})>'


class Graph(ABC):
    """Abstract graph implementation."""
    @abstractmethod
    def vertices(self) -> List[Vertex]:
        """Get all vertices."""
        pass

    @abstractmethod
    def edges(self) -> List[Edge]:
        """Get all edges."""
        pass

    @abstractmethod
    def add_vertex(self, v: Vertex) -> None:
        """Insert a vertex."""
        pass

    @abstractmethod
    def remove_vertex(self, v: Vertex) -> None:
        """Remove a vertex."""
        pass

    @abstractmethod
    def are_adjacent(self, v: Vertex, w: Vertex) -> bool:
        """True if vertices v and w are adjacent."""
        pass

    @abstractmethod
    def add_edge(self, e: Edge, v: Vertex, w: Vertex) -> None:
        """Insert an edge between vertex1 and vertex2."""
        pass

    @abstractmethod
    def remove_edge(self, e: Edge) -> None:
        """Remove an edge."""
        pass


class AdjacencyVertex(Vertex):
    def __init__(self, key: str, neighbours=None) -> None:
        super().__init__(key)
        self._neighbours: List[Vertex] = neighbours if neighbours is not None else []


class AdjacencyListArray(Graph):
    """An array backed implementation of an Adjacency List Graph."""
    def __init__(self, adjacency_list=None) -> None:
        self._vertices = []
        if adjacency_list is not None:
            for vertices in adjacency_list:
                self.add_vertex(vertices)

    def vertices(self) -> List[Vertex]:
        """Get all vertices."""
        vertices: Dict[str, Vertex] = {}
        for i, neighbours in enumerate(self._vertices):
            i = str(i)
            if i in vertices:
                vertex = vertices[i]
            else:
                vertex = AdjacencyVertex(i)
                vertices[i] = vertex

            for n in neighbours:
                n = str(n)
                if n in vertices:
                    neighbour = vertices[n]
                else:
                    neighbour = AdjacencyVertex(n)
                    vertices[n] = neighbour
                vertex.add_neighbour(neighbour)
        return list(vertices.values())

    def edges(self) -> List[Edge]:
        """Get all edges."""
        edges: List[Edge] = []
        # @todo fix
        for vertex in self._vertices:
            pass
        #     edge = Edge(v, w)
        #     edges.append(edge)
        return edges

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
        return False

    def add_edge(self, e: Edge, v: Vertex, w: Vertex) -> None:
        """Insert an edge between two vertices."""
        pass

    def remove_edge(self, e: Edge) -> None:
        """Remove an edge."""
        pass


def get_graph():
    graph = AdjacencyListArray([[1, 2], [2, 3], [4], [4, 5], [5], []])
    return graph
