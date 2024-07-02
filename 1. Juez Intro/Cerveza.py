# Más de 46: MUY BUENA
# • Entre 36 y 46: BUENA
# • Entre 21 y 35: REGULAR
# • Entre 11 y 20: MALA
# • Entre 0 y 10: CRUZCAMPO

ibu = int(input())

if ibu > 46:
    print("MUY BUENA")
elif 36 <= ibu <= 46:
    print("BUENA")
elif 21 <= ibu <= 35:
    print("REGULAR")
elif 11 <= ibu <= 20:
    print("MALA")
else:
    print("CRUZCAMPO")