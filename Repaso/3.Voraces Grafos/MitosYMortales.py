from random import randint


def distanciaMinima(li, visited):
    node = -1
    dist = float("inf")
    for i in range(0, len(li)):
        if not visited[i] and li[i] < dist:
            dist = li[i]
            node = i

    return node, dist


def prim(l, NN):
    coste_total = 0
    visitados = [False] * NN
    candidates = [float("inf")] * NN
    inicial = randint(0, NN-1)
    visitados[inicial] = True

    for nd, di in l[inicial]:
        candidates[nd] = di

    for i in range(1, NN):

        nextNode, dist = distanciaMinima(candidates, visitados)

        if dist < float("inf"):
            coste_total += dist
            visitados[nextNode] = True

        for nd, di in l[nextNode]:

            if not visitados[nd]:
                candidates[nd] = min(candidates[nd], di)

    return coste_total


N, M = map(int, input().strip().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    n1, n2, d = map(int, input().strip().split())
    arr[n1].append([n2, d])
    arr[n2].append([n1, d])

sol = prim(arr, N)
solucion = (sol // 5)
if solucion < (sol / 5):
    solucion = solucion + 1
print(solucion)
