def backpack(l, e):
    lord = sorted(l, key=lambda x: x[0] / x[1], reverse=True)
    daño = 0
    for hechizo in lord:

        if e == 0:
            break
        elif hechizo[1] <= e:
            daño += hechizo[0]
            e -= hechizo[1]
        else:
            daño += hechizo[0] / hechizo[1] * e
            break

    return daño


e1, e2, n = map(int, input().strip().split())
ma1 = []
ma2 = []
for i in range(n):
    d1, m1, d2, m2 = map(int, input().strip().split())
    ma1.append([d1, m1])
    ma2.append([d2, m2])

vm1 = backpack(ma1, e1)
vm2 = backpack(ma2, e2)
print("{:.2f} {:.2f}".format(vm1,vm2))



