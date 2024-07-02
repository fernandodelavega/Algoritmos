def dyv(p, arrS, arrC):
    start = 0
    end = len(arrC) - 1

    while start <= end:
        mid = (start + end) // 2
        if arrC[mid][0] <= p:

            if arrC[mid][0] == p:

                if arrC[mid] not in arrS:
                    return arrC[mid]
                else:
                    return chekeo(mid, arrS, arrC)
            elif arrC[mid + 1][0] == p:

                if arrC[mid + 1] not in arrS:
                    return arrC[mid + 1]
                else:
                    return chekeo(mid + 1, arrS, arrC)

            elif arrC[mid + 1][0] > p:
                return [-1, "No existe"]

            else:
                start = mid + 1
        else:
            end = mid - 1

    return [-1, "No existe"]


def chekeo(x, arrS, arrC):
    i = x
    j = x
    while i >= 0 or j <= len(arrC):
        i -= 1
        j += 1
        if j <= len(arrC) and arrC[j] not in arrS:
            return arrC[j]
        elif i >= 0 and arrC[i] not in arrS:
            return arrC[i]

    return [-1, "No hay recompensa"]


ncajas = int(input().strip())
arrayC = []

for _ in range(ncajas):
    numero, nombre = map(str, input().strip().split())
    arrayC.append([int(numero), nombre])

participantes = int(input().strip())
arraySoluciones = []

for _ in range(participantes):
    persona = int(input().strip())
    arraySoluciones.append(dyv(persona, arraySoluciones, arrayC))

for _ in range(len(arraySoluciones)):
    print(arraySoluciones[_][1])
