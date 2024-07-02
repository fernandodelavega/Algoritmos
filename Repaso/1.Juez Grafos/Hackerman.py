from collections import deque


def dfs(node, L, visited):
    cola = deque()
    visited[node] = True
    cola.append(node)

    while cola:
        actual = cola.pop()
        for vecino in L[actual]:
            if not visited[vecino]:
                visited[vecino] = True
                cola.append(vecino)


def busquedaConexas(L, N, primero):
    visited = [False] * N
    contador = 0
    visited[0] = primero
    for nodo in range(N):

        if not visited[nodo]:
            dfs(nodo, L, visited)
            contador += 1

    return contador


Nodos, Caminos = map(int, input().strip().split())

costes = []
adList = []
total = 0

for n in range(Nodos):
    coste = int(input().strip())
    costes.append(coste)
    adList.append([])

for m in range(Caminos):
    a, b = map(int, input().strip().split())

    adList[a].append(b)
    adList[b].append(a)

for node in range(Nodos):
    auxVar = adList[node]
    adList[node] = []
    if node == 0:
        nConexas = busquedaConexas(adList, Nodos, True)
    else:
        nConexas = busquedaConexas(adList, Nodos, False)

    if nConexas > 1:
        total += costes[node]
    adList[node] = auxVar

print(total)

