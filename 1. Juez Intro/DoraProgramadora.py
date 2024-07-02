# Entrada
# La entrada serán números enteros � que representa el identificador del empleado que ha
# mirado una red social. El último número siempre será -1.
# Salida
# Se imprimirá por pantalla el identificador de cada empleado que haya mirado 3 o más
# veces una red social.

registros = {}
entrada = input()
valores = entrada.split()
salida = []
for identificador in valores:
    identificador = int(identificador)

    if identificador != -1:
        if identificador in registros:
            registros[identificador] += 1
        else:
            registros[identificador] = 1
    else:
        break

# Imprimir empleados que han accedido más de 3 veces

for empleado, contador in registros.items():
    if contador >= 3:
        salida.append(empleado)
print(*sorted(salida))
