from collections import deque
def searchGroups(L, N):
    visited = set()
    grupos = []

    for nodo in range(N):
        if nodo not in visited:
            grupo = []
            cola = deque()
            cola.append(nodo)

            while cola:
                actual = cola.pop()
                if actual not in visited:
                    grupo.append(actual)
                    visited.add(actual)
                    cola.extend(L[actual])
            grupos.append(grupo)
    return len(grupos)


Nodos, Caminos = map(int, input().split())
lista = [[] for _ in range(Nodos)]

for i in range(Caminos):
    a, b = map(int, input().split())
    lista[a].append(b)

    lista[b].append(a)

print(searchGroups(lista, Nodos))
