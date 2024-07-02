from random import randint


def selectMin(candidates, visited):
    vertex = None
    weight = float('inf')
    for i in range(0, len(candidates)):
        if not visited[i] and candidates[i] < weight:
            vertex = i
            weight = candidates[i]
    return vertex, weight


def prim(g):
    n = len(g)
    initial = randint(0, len(g) - 1)
    visited = [False] * n
    sol = 0
    visited[initial] = True

    candidates = [float('inf')] * n
    for (start, end, weight) in g[initial]:
        candidates[end] = weight

    for i in range(1, n):
        nextNode, cost = selectMin(candidates, visited)
        if cost < float('inf'):
            sol += cost
            visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if not visited[end]:
                candidates[end] = min(weight, candidates[end])
    return sol


n, m = map(int, input().strip().split())
g = []
for i in range(n):
    g.append([])
for i in range(m):
    u, v, d = map(int, input().strip().split())
    g[u].append((u, v, d))
    g[v].append((v, u, d))

sol = prim(g)

solucion = (sol // 5)
if solucion < (sol / 5):
    solucion = solucion + 1
print(solucion)
