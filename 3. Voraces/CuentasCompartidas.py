def sack(plat, cas):
    beneficio = 0
    gasto = cas
    for j in range(len(plat)):
        if plat[j][2] <= gasto:
            beneficio += plat[j][1]
            gasto -= plat[j][2]
        elif gasto > 0:
            beneficio += plat[j][1] / plat[j][2] * gasto
            return beneficio

    return beneficio


A, P = map(int, input().strip().split())
platformas = []
cash = []
beneT = 0
for _ in range(P):
    nombre, satisfacion, coste = input().strip().split()
    platformas.append([nombre, int(satisfacion), int(coste)])

for _ in range(A):
    cash.append(int(input().strip()))


platformas.sort(key=lambda x: x[1]/x[2], reverse=True)


for i in range(A):
    if i != 0:
        beneT += sack(platformas, cash[i])

print("{0:.2f}".format(beneT))
