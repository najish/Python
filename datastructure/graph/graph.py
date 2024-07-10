import networkx as nx


graph = nx.Graph()

graph.add_node(10)
graph.add_node(20)
graph.add_node(30)
graph.add_node(40)
graph.add_edge(10,20)


graph.adjacency()

print(graph.is_directed())