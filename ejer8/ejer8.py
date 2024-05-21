import itertools

nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


caminos = list(itertools.permutations(nodos))


for camino in caminos:
    print(camino)


