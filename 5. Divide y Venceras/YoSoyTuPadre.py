from collections import deque


def calcular_generaciones(familia, consultas):
    # Diccionario que representa el árbol genealógico
    arbol = {}
    # Conjunto de todos los miembros del árbol
    todos_los_miembros = set()
    # Conjunto de todos los hijos de los miembros
    todos_los_hijos = set()
    # Diccionario para almacenar el nivel o generación de cada miembro
    niveles = {}

    # Llenar el árbol genealógico
    for miembro, *hijos in familia:
        arbol[miembro] = hijos
        todos_los_miembros.add(miembro)
        # Añadir los hijos al conjunto
        for hijo in hijos:
            todos_los_hijos.add(hijo)

    # Identificar la raíz
    # La raíz será el miembro que está en todos_los_miembros pero no en todos_los_hijos
    raiz = list(todos_los_miembros - todos_los_hijos)
    # Asegurarnos de tener solo una raíz, tomamos el primer elemento
    if raiz:
        raiz = raiz[0]
    else:
        raise ValueError("No se encontró la raíz del árbol.")

    # Inicializar una cola para el BFS desde la raíz
    cola = deque([raiz])
    niveles[raiz] = 1  # La raíz es de nivel 1 (1ª generación)

    # Realizamos BFS para calcular el nivel de cada miembro
    while cola:
        miembro_actual = cola.popleft()
        nivel_actual = niveles[miembro_actual]

        # Procesar los hijos del miembro actual
        if miembro_actual in arbol:
            for hijo in arbol[miembro_actual]:
                if hijo not in niveles:  # Solo procesar si no hemos visto al hijo antes
                    niveles[hijo] = nivel_actual + 1
                    cola.append(hijo)

    # Ahora, para las consultas, devolvemos el nivel de cada miembro solicitado
    resultados = []
    for consulta in consultas:
        # Obtener el nivel del miembro consultado
        nivel = niveles.get(consulta, -1)
        resultados.append(nivel)

    return resultados


# Entrada
N = int(input().strip())
familia = []
for _ in range(N):
    linea = list(map(int, input().strip().split()))
    familia.append(linea)

M = int(input().strip())
consultas = []
for _ in range(M):
    consulta = int(input().strip())
    consultas.append(consulta)

# Proceso de generación y salida de resultados
resultados = calcular_generaciones(familia, consultas)
for resultado in resultados:
    print(resultado)
