def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem


def dijkstra(g, origin):
    n = len(g) - 1
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
    ###################################

    for _ in range(1, n):  # Bucle voraz
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True

        for start, end, weight in g[nextNode]:
            distances[end] = min(distances[end], distances[start] + weight)

    ###################################
    sumT = 0
    for k in range(len(distances)):
        sumT += distances[k]

    return sumT


N, M = map(int, input().strip().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    n1, n2, d = map(int, input().strip().split())
    arr[n1].append([n1, n2, d])
    arr[n2].append([n2, n1, d])

sol = []
minT = float("inf")
for _ in range(N):
    x = dijkstra(arr, _)
    sol.append(x)
    if x < minT:
        minT = x

print(minT)
for _ in range(len(sol)):
    print(str(_) + ": " + str(sol[_]))
