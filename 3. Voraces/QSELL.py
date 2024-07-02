def ordCand(cla, pa):
    ele = sorted(pa, key=lambda x: x[cla] / x[4], reverse=True)
    return ele


def knapsack(elegidos, time, c):
    beneficioT = 0
    eleg = []
    for elegido in elegidos:
        if elegido[4] <= time:
            eleg.append(elegido[0])
            beneficioT += elegido[c]
            time -= elegido[4]

        elif elegido[4] > time > 0:
            eleg.append(elegido[0])
            beneficioT += (elegido[c] / elegido[4]) * time
            return beneficioT, eleg

    return beneficioT, eleg


nC = int(input().strip())

for i in range(nC):
    clave = -1
    parejasL = []
    cl = input().strip()
    tiempo = int(input().strip())
    parejas = int(input().strip())

    for j in range(parejas):
        name, b, i, k, t = map(str, input().strip().split())
        parejasL.append((name, int(b), int(i), int(k), int(t)))

    if cl == 'kindness':
        clave = 3
    elif cl == 'beauty':
        clave = 1
    else:
        clave = 2

    cand = ordCand(clave, parejasL)
    beneficioF, elegidosF = knapsack(cand, tiempo, clave)

    for y in elegidosF:
        print(y, end=' ')
    print()

    print("%.2f" % beneficioF)
