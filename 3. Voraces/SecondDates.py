def selec(cand, k):
    cand = sorted(cand, key=lambda x: x[1])
    s1 = []
    s2 = []

    for j in range(len(cand)):
        if j < k:
            s1.append(cand[j][0])
        else:
            s2.append(cand[j][0])

    return s1, s2


N, K = list(map(int, input().strip().split()))
candidatos = []

for i in range(N):
    nombre, edad = list(map(str, input().strip().split()))
    candidatos.append([nombre, int(edad)])

jovenes, no_jovenes = selec(candidatos, K)

print(*jovenes)
print(*no_jovenes)
