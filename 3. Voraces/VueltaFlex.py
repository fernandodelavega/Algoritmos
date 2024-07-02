def maxPaises(mess, paises):
    fin = 0
    p = []
    pp = []
    for j in range(paises):
        p.append([mess[j*2], mess[j*2 + 1]])
    p = sorted(p, key=lambda x: x[1])

    for pais in p:
        if pais[0] >= fin:
            pp.append(pais)
            fin = pais[1]

    return len(pp)


V = int(input())  # Número de posibles organizaciones
itinerarios = []
maxPPP = []
for i in range(V):
    P = int(input())  # Número de países en el itinerario
    meses = list(map(int, input().split()))  # Meses para cada país
    maxPP = maxPaises(meses, P)
    maxPPP.append(maxPP)

for i in range(len(maxPPP)):
    print(maxPPP[i])