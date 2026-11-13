from collections import deque

# Diagram 2: Graph (undirected)
# Edges: B-A, B-I, B-R, I-R, I-D, A-D, A-T, T-O, O-D


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, v):
        self.adjacency.setdefault(v, [])

    # Neighbors are visited in the order they are added.
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)

    # BFS using a queue and a visited set
    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in self.adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return " - ".join(result)

    # DFS using recursion and a visited set
    def dfs(self, start):
        result = []
        self._dfs_visit(start, set(), result)
        return " - ".join(result)

    def _dfs_visit(self, v, visited, result):
        visited.add(v)
        result.append(v)
        for neighbor in self.adjacency[v]:
            if neighbor not in visited:
                self._dfs_visit(neighbor, visited, result)


def get_results():
    g = Graph()

    # B: A, I, R | A: B, T, D | I: B, R, D | R: B, I
    # D: A, I, O | T: A, O    | O: T, D
    g.add_edge("B", "A")
    g.add_edge("B", "I")
    g.add_edge("B", "R")
    g.add_edge("A", "T")
    g.add_edge("A", "D")
    g.add_edge("I", "R")
    g.add_edge("I", "D")
    g.add_edge("D", "O")
    g.add_edge("T", "O")

    return g.bfs("B"), g.dfs("B")


def run():
    bfs_text, dfs_text = get_results()
    print("+------------------+")
    print("|      Graph       |")
    print("+------------------+")
    print(f"BFS: {bfs_text}")
    print(f"DFS: {dfs_text}")


if __name__ == "__main__":
    run()