# Search methods

import search

ab = search.GPSProblem('O', 'U'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bounds_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450



# Tarea
# 1. Imprimir el numero de nodos visitados
# 2. Imprimir nº nodos expandidos ∫
# 3. Contar tamaño maximo que alcanza la lista abierta