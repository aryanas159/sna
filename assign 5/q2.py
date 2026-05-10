import networkx as nx

V = [1, 2, 3, 4, 5, 6]
E = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6)]
G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

def greedy_independent_set(graph, selection_order):
    independent_set = []
    remaining_nodes = list(selection_order)
    
    while remaining_nodes:
        v = remaining_nodes.pop(0)
        independent_set.append(v)
        
        neighbors = list(graph.neighbors(v))
        remaining_nodes = [node for node in remaining_nodes if node not in neighbors]
            
    return independent_set

order_a = [1, 2, 3, 4, 5, 6]
set_a = greedy_independent_set(G, order_a)

print(f"Sequence of selections: {set_a}")
print(f"Resulting Maximal Independent Set: {set_a}")

order_b = [4, 1, 6]
set_b = greedy_independent_set(G, order_b + [v for v in V if v not in order_b])
print(f"Alternative sequence: {set_b}")