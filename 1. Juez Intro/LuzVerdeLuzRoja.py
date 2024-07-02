# Un usuario será eliminado si la luz es roja y ha activado el sensor.
# Entrada
# La entrada se compone de un entero 𝑁, que indica el identificador del usuario, un carácter
# 𝐶, que vale ‘v’ si la luz es verde y ‘r’ si es roja, y un entero 𝐴 que vale 1 si ha activado el
# sensor y 0 si no lo ha activado.

# Salida
# Se debe imprimir la cadena “JUGADOR XXX ELIMINADO” si el usuario ha activado
# el sensor durante la luz roja o “JUGADOR XXX CONTINUAR” en cualquier otro caso,
# siendo XXX el identificador del jugador. El identificador siempre tendrá tres cifras tal y
# como se lee de la entrada.

n, l, s = map(str, input().strip().split())
bool_s = int(s)

if (l == 'r') and (bool_s == 1):
    print('JUGADOR ' + n + ' ELIMINADO')
else:
    print('JUGADOR ' + n + ' CONTINUAR')
