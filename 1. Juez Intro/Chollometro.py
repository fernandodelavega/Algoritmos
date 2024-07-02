
cupon = list(map(int,(input().strip().split())))
M = 0
P = 0

for i in range(len(cupon)):
    if(cupon[i] > P):
        P = cupon[i]
        M = i + 1
    print(i+1,end=" ")
    for j in range(cupon[i]):
        print("=",end="")
    print()
print("El mas usado es el cupon ", M, " con ", P, " usos")