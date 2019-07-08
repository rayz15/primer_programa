numero_inicial = 10
if numero_inicial % 2 == 0:
    print(numero_inicial)
    print("numero inicial es numero par tambien")
while numero_inicial > 0:
    numero_inicial -= 1
    print(numero_inicial)
    if numero_inicial % 2 == 0:
        print("es un numero par")
    else:
        print("es un numero impar")

print("eso fue todo bye")
