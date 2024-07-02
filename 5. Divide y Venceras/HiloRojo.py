def dYV(data, ini, fin, search):
    if ini > fin:
        return -1
    else:
        half = (ini + fin) // 2
        if search == data[half]:
            return half
        else:
            if search > data[half]:
                return dYV(data, half + 1, fin, search)
            else:
                return dYV(data, ini, half - 1, search)


n = int(input().strip())
data1 = list(map(int, input().strip().split()))
m = int(input().strip())
data2 = list(map(int, input().strip().split()))

p = int(input().strip())

for _ in range(p):
    q1, q2 = map(int, input().strip().split())
    p1 = dYV(data1, 0, n - 1, q1)
    p2 = dYV(data2, 0, m - 1, q2)

    if p1 >= 0 and p2 >= 0:
        print(str(p1), str(p2), end="\n")
    else:
        print("SIN DESTINO", end="\n")
