def organizar_horario(actividades):
    actividades.sort(key=lambda x: x[2])  # Ordenar actividades por hora de finalización
    horario = []
    fin_actividad = 0

    for actividad in actividades:
        if actividad[1] >= fin_actividad:
            horario.append(actividad)
            fin_actividad = actividad[2]

    return len(horario)


activities = []
n = int(input())

for k in range(n):
    name, i, f = map(str, input().split())
    activities.append((name, int(i), int(f)))

maxact = organizar_horario(activities)
print(maxact)
