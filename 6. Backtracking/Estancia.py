def bt(objetos, mochila, selected, actCost, actProfit, bestProfit, bestCost, bestMochila, x):
    if esSolucion(mochila, actCost, objetos):
        if actProfit > bestProfit:
            bestProfit = actProfit
            bestCost = actCost
            bestMochila = mochila.copy()
        return bestMochila, bestProfit, bestCost
    else:
        for k in range(x, len(objetos)):
            o = objetos[k]
            if esFactible(o, selected, actCost):
                mochila.append(o)
                selected.add(o)
                actCost += o[1]
                actProfit += o[2]
                bestMochila, bestProfit, bestCost = bt(objetos, mochila, selected, actCost, actProfit, bestProfit,
                                                       bestCost, bestMochila, k + 1)
                mochila.pop()
                selected.remove(o)
                actCost -= o[1]
                actProfit -= o[2]
    return bestMochila, bestProfit, bestCost


def esSolucion(mochila, actCost, objetos):
    min_peso = 0x3f3f3f
    for o in objetos:
        if o not in mochila and min_peso > o[1]:
            min_peso = o[1]
    return actCost + min_peso > P


def esFactible(o, selected, actCost):
    return actCost + o[1] <= P and (o not in selected)


N, P, B = map(int, input().strip().split())
objetos = []

for _ in range(N):
    O, C, G = input().strip().split()
    objetos.append((O, int(C), int(G)))
mochila = []
selected = set()

mejorMochila, mejorProfit, mejorCost = bt(objetos, mochila, selected, 0, 0, 0, 0, [], 0)
mejorMochila.sort()

for o in mejorMochila:
    print(o[0], end=' ')
print()

print(mejorCost,mejorProfit)
if mejorProfit > B:
    print("SE VA")
else:
    print("VUELVE")
