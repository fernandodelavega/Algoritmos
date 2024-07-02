# Entrada
# La primera línea se compone de un entero 𝑁 que indica el número de usuarios con los
# que se va a probar el match. La segunda línea tendrá una cadena de caracteres con el
# nombre del usuario que busca pareja. Las siguientes 𝑁 líneas tendrán una cadena de
# caracteres en cada línea, que representa el nombre del candidato a ser pareja.
# Salida
# Se deberá imprimir, por cada candidato, “ITS A MATCH!” en caso de que el perfil
# encaje, o “NEXT!” en caso contrario

def contar_vocales(cad):
    voc = 0
    for c in cad:
        if c in "aeiouAEIOU":
            voc = voc + 1
    return voc

N = int(input().strip())
S = contar_vocales(str(input().strip()))
P = []

for i in range(N):
    P.append(contar_vocales(input().strip()))

for i in range(N):
    if P[i] == S:
        print("ITS A MATCH!")
    else:
        print("NEXT!")


