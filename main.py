import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

num_nodes = 50
edge_probability = 0.35

G = nx.erdos_renyi_graph(num_nodes, edge_probability)

average_degree_actual = np.mean([deg for _, deg in G.degree()])

average_degree_theoretical = (num_nodes - 1) * edge_probability

print(f"Сгенерированный граф:")
print(f"- Количество вершин: {num_nodes}")
print(f"- Вероятность ребра: {edge_probability}")
print(f"Средняя степень вершины (сгенерированная): {average_degree_actual:.2f}")
print(f"Средняя степень вершины (теоретическая): {average_degree_theoretical:.2f}")


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.title("Граф по модели Эрдёша-Реньи")
plt.savefig("my_graph.png", format='png')
plt.show()
# Проверка, что прим многократной геренрации будет +- тоже, что в теории
num_simulations = 100
average_degrees = []
for _ in range(num_simulations):
    G = nx.erdos_renyi_graph(num_nodes, edge_probability)
    average_degrees.append(np.mean([deg for _, deg in G.degree()]))
print(f"Средняя степень (по симуляциям): {np.mean(average_degrees):.2f}")