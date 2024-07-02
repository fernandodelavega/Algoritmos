def sortList(L, K):
    return sorted(L, key=lambda x: x[K] / x[4], reverse=True)

def knapsack(L, t, K):
    elegidos = []
    beneficioT = 0
    for concursante in L:

        if concursante[4] < t:
            beneficioT += concursante[K]
            elegidos.append(concursante[0])
            t -= concursante[4]
        else:
            beneficioT += concursante[K] / concursante[4] * t
            elegidos.append(concursante[0])
            t -= concursante[4]
            return elegidos, beneficioT


    return elegidos, beneficioT


n_concursante = int(input().strip())

for _ in range(n_concursante):
    cualidad = input().strip()
    tmax = int(input().strip())
    n_parejas = int(input().strip())
    parejas = []
    k_cualidad = 0
    for j in range(n_parejas):
        nombre, b, i, k, t = map(str, input().strip().split())
        parejas.append([nombre, int(b), int(i), int(k), int(t)])

    if cualidad == "beauty":
        k_cualidad = 1
    elif cualidad == "intelligence":
        k_cualidad = 2
    elif cualidad == "kindness":
        k_cualidad = 3

    parejas = sortList(parejas, k_cualidad)

    elegidos, beneficioT = knapsack(parejas, tmax, k_cualidad)

    for y in elegidos:
        print(y, end=' ')
    print('')

    print("%.2f" % beneficioT)
