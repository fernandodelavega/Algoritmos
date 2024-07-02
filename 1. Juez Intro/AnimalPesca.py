# Entrada
# La entrada se compone de un entero 𝐶, que indica el número de capturas realizadas, y a
# continuación, 𝑁 líneas con dos números 𝐼 y 𝑆 que indican el identificador del pez y la
# puntuación asociada, respectivamente.

# Salida
# Se deben imprimir tres enteros separados por un espacio que indican el identificador de
# la mejor captura, el de la segunda mejor captura, y la suma de la puntuación de las dos
# mejores capturas.

def obtener_mejores_capturas(num_capturas):
    mejores_capturas = []
    for _ in range(num_capturas):
        identificador, puntuacion = map(int, input().split())
        mejores_capturas.append((identificador, puntuacion))

    mejores_capturas.sort(key=lambda x: x[1], reverse=True)
    suma_puntuaciones = mejores_capturas[0][1] + mejores_capturas[1][1]
    return mejores_capturas[0][0], mejores_capturas[1][0], suma_puntuaciones


# Lectura de la entrada
num_capturas = int(input())
resultado = obtener_mejores_capturas(num_capturas)

# Impresión de la salida
print(*resultado)
