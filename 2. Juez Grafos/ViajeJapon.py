

def dfs(graph, city, visited):
    if city in graph:

        visited.add(city)

        for neighbor in graph[city]:

            if neighbor not in visited:

                dfs(graph, neighbor, visited)

                # if not dfs(graph, neighbor, visited):
                #     #return False
                #     pass

    return True


def check_itinerary(N, M, connections):
    graph = {}

    for connection in connections:

        city1, city2 = connection

        if city1 not in graph:
            graph[city1] = []

        graph[city1].append(city2)

    visited = set()

    # if not dfs(graph, 1, visited):
    #     return "CAMBIA EL ITINERARIO"

    dfs(graph, 0, visited)

    if len(visited) != N:
        return "CAMBIA EL ITINERARIO"

    return "PERFECTO"


# Lectura de la entrada

Nodes, Roads = map(int, input().split())

listRoads = []

for i in range(Roads):
    U, V = map(int, input().split())

    listRoads.append([U, V])

# Verificación del itinerario

result = check_itinerary(Nodes, Roads, listRoads)

# Impresión de la salida

print(result)
