def backtrack(current_node, visited, current_distance, max_distance, distance_matrix, N):
    """
    current_node: el nodo actual desde el cual explorar.
    visited: un conjunto de nodos visitados.
    current_distance: la distancia actual recorrida.
    max_distance: una lista con un solo elemento que almacena la máxima distancia encontrada.
    distance_matrix: matriz de distancias entre los nodos.
    N: número total de nodos.
    """
    # Si todos los nodos han sido visitados, verifica si podemos volver al nodo de origen (0)
    if len(visited) == N:
        # Verificar si el ciclo puede cerrarse volviendo al nodo 0
        if distance_matrix[current_node][0] > 0:
            total_distance = current_distance + distance_matrix[current_node][0]
            # Actualizar la máxima distancia encontrada
            if total_distance > max_distance[0]:
                max_distance[0] = total_distance
        return

    # Explora desde el nodo actual
    for next_node in range(N):
        if next_node not in visited and distance_matrix[current_node][next_node] > 0:
            # Marcar el nodo como visitado
            visited.add(next_node)
            # Llamar recursivamente para continuar explorando desde el siguiente nodo
            backtrack(next_node, visited, current_distance + distance_matrix[current_node][next_node], max_distance,
                      distance_matrix, N)
            # Retroceder: desmarcar el nodo como visitado
            visited.remove(next_node)


def find_max_distance(distance_matrix):
    N = len(distance_matrix)  # Número total de nodos
    max_distance = [0]  # Lista con un solo elemento para almacenar la máxima distancia encontrada

    # Iniciar backtracking desde el nodo 0
    visited = set([0])
    backtrack(0, visited, 0, max_distance, distance_matrix, N)

    # Devolver la máxima distancia encontrada
    return max_distance[0]


# Leer los datos de entrada
n = int(input().strip())  # Número de puntos de venta
points = []
for _ in range(n):
    points.append(list(map(int, input().strip().split())))

# Ejecutar la función tsp_max_distance
print(find_max_distance(points))
