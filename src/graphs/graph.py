from abc import ABC, abstractmethod
from typing import List


class Vertex:
    """A graph vertex."""
    def __init__(self, key) -> None:
        super().__init__()
        if not isinstance(key, (str, int, float)):
            raise ValueError('Key must be a scalar value')
        self._key = key
        self._neighbours: List[Vertex] = []

    def key(self):
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
