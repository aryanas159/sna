import networkx as nx

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
G = nx.Graph(adj_list)
G_complement = nx.complement(G)


all_maximal_independent_sets = list(nx.find_cliques(G_complement))

all_maximal_independent_sets = [sorted(s) for s in all_maximal_independent_sets]

print(f"(a) All Maximal Independent Sets: {all_maximal_independent_sets}")

max_size = max(len(s) for s in all_maximal_independent_sets)
maximum_sets = [s for s in all_maximal_independent_sets if len(s) == max_size]

print(f"(b) Maximum Independent Set(s): {maximum_sets}")
print(f"(c) Multiple maximum sets exist? {'Yes' if len(maximum_sets) > 1 else 'No'}")