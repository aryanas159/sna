import networkx as nx

V = ['A', 'B', 'C', 'D', 'E', 'F']
E = [('A', 'D'), ('A', 'E'), ('B', 'D'), ('C', 'E'), ('C', 'F')]

G = nx.Graph()
G.add_edges_from(E)

max_matching = nx.matching.max_weight_matching(G, maxcardinality=True)

print(f"Maximum Matching: {max_matching}")
print(f"Size: {len(max_matching)}")