import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos para los miembros de la familia
familia = ['Abuelo1', 'Abuela1', 'Abuelo2', 'Abuela2','Tio', 'Tia', 'Padre', 'Mama', 'Primo', 'Hijo']
G.add_nodes_from(familia)

# Añadir bordes para representar las relaciones familiares
G.add_edge('Abuelo1', 'Padre')
G.add_edge('Abuela1', 'Padre')
G.add_edge('Abuelo2', 'Mama')
G.add_edge('Abuela2', 'Mama')
G.add_edge('Abuelo1', 'Tio')
G.add_edge('Abuela1', 'Tio')
G.add_edge('Tio', 'Primo')
G.add_edge('Tia', 'Primo')
G.add_edge('Padre', 'Hijo')
G.add_edge('Mama', 'Hijo')

# Dibujar el grafo
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=40)  # Posiciones para todos los nodos
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrows=True)
plt.title("Estructura Familiar")
plt.show()