def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates

def updateComponents(components, new_id, old_id):
    for i in range(0, len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g):
    candidates = sortCandidates(g)
    components = list(range(len(g)))
    count = len(components) - 1
    sol = 0
    pesos = [0] * len(g)
    i = 0
    while count > 0 and len(candidates) > i:
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            sol += weight
            count -= 1
            updateComponents(components, components[start], components[end])
            pesos[start] += weight
            pesos[end] += weight
        i += 1
    return sol, pesos

n, m = map(int, input().strip().split())
g = []

for _ in range(n):
    g.append([])
for _ in range(m):
    u, v, d = map(int, input().strip().split())
    g[u].append((u, v, d))
    g[v].append((v, u, d))

sol, weights = kruskal(g)

for i in range(len(weights)):
    print("C"+ str(i) +" -> " + str(weights[i]))

print("Esfuerzo realizado -> " + str(sol))