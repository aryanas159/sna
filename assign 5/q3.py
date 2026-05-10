import networkx as nx

edges = [
    ('S1', 'P1'), ('S1', 'P2'),
    ('S2', 'P1'),
    ('S3', 'P2'), ('S3', 'P3'),
    ('S4', 'P3')
]

B = nx.Graph()
B.add_edges_from(edges)

def get_maximal_matching(graph):
    matching = set()
    used_nodes = set()
    for u, v in graph.edges():
        if u not in used_nodes and v not in used_nodes:
            matching.add((u, v))
            used_nodes.add(u)
            used_nodes.add(v)
    return matching

maximal = get_maximal_matching(B)

maximum = nx.bipartite.matching.hopcroft_karp_matching(B, top_nodes=['S1', 'S2', 'S3', 'S4'])
maximum_set = {tuple(sorted(items)) for items in maximum.items() if items[0].startswith('S')}

print(f"Maximal Matching: {maximal}")
print(f"Maximum Matching: {maximum_set}")