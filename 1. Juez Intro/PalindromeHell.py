N = int(input().strip())
a_p = int(N/2)
m_p = int(N/2)
gana = "EMPATE"

for i in range(N):
    palabra = input().lower().strip()
    if palabra != palabra[::-1]:
        if i % 2 == 0:
            a_p -= 1
            if gana == "EMPATE":
                gana = "MONICA"
        else:
            m_p -= 1
            if gana == "EMPATE":
                gana = "ANA"

print(a_p, m_p, gana)


