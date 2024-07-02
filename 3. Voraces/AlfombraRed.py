def alfaorder(fam):
    famosos_O = sorted(fam, key=lambda y: y[0])
    return famosos_O[0]


# Lectura de la entrada
tiempoT = 0
x = True
N = int(input())
famosos = []
for _ in range(N):
    nombre, amabilidad, fama, tiempo = input().split()
    amabilidad = int(amabilidad)
    fama = int(fama)
    tiempo = int(tiempo)
    famosos.append((nombre, amabilidad, fama, tiempo))

# Ordenar los famosos según la prioridad
famosos_ordenados = sorted(famosos, key=lambda z: -z[2] / z[1])
primer = alfaorder(famosos)

# Imprimir los nombres de los famosos ordenados
for famoso in famosos_ordenados:
    print(famoso[0])
    if famoso == primer:
        x = False
    if famoso != primer and x:
        tiempoT += famoso[3]

# Calcular el tiempo que debe esperar el primer famoso alfabéticamente

print(tiempoT)
