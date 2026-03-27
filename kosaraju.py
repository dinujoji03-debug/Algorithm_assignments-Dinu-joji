# Program to find SCCs using Kosaraju’s Algorithm

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def fill_order(self, v, visited, stack):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.fill_order(neighbour, visited, stack)
        stack.append(v)

    def get_transpose(self):
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g

    def dfs(self, v, visited, component):
        visited.add(v)
        component.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, component)

    def find_scc(self):
        stack = []
        visited = set()

        # Step 1: Fill stack
        for vertex in self.V:
            if vertex not in visited:
                self.fill_order(vertex, visited, stack)

        # Step 2: Transpose graph
        transpose_graph = self.get_transpose()

        # Step 3: DFS in stack order
        visited.clear()
        scc_list = []

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                transpose_graph.dfs(v, visited, component)
                scc_list.append(component)

        return scc_list


# ---- Construct Graph Exactly as Given ----

vertices = ['a','b','c','d','e','f','g','h']
g = Graph(vertices)

edges = [
    ('a','b'),
    ('b','c'),
    ('b','d'),
    ('c','a'),
    ('c','e'),
    ('d','c'),
    ('d','e'),
    ('e','f'),
    ('f','d'),
    ('f','g'),
    ('g','e'),
    ('g','h'),
    ('h','f')
]

for u, v in edges:
    g.add_edge(u, v)

# ---- Find SCCs ----
sccs = g.find_scc()

print("Strongly Connected Components (SCCs)")
print("------------------------------------")

output_lines = []
output_lines.append("Strongly Connected Components (SCCs)")
output_lines.append("------------------------------------")

for i, component in enumerate(sccs, 1):
    comp_str = "{ " + ", ".join(component) + " }"
    line = f"SCC {i}: {comp_str}"
    print(line)
    output_lines.append(line)

# Save to file
with open("scc_results.txt", "w") as file:
    for line in output_lines:
        file.write(line + "\n")

print("\nOutput saved to scc_results.txt")
