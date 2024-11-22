import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    (0, 1),
    (0, 2),
    (0, 3)
])
centrality = nx.eigenvector_centrality_numpy(G)
print("Центральности и их вектора:")
for node, value in centrality.items():
    print(f"Узел {node}: центральность {value:.4f}")

# Визуализируем график с использованием библиотеки matplotlib
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=15)
plt.title("Граф")
plt.savefig("my_graph.png", format='png')
plt.show()
