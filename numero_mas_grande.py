numeros_usuario = []
numeros_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numeros_del_usuario.isdigit():
        numeros_del_usuario = input("Escribe un numero: ")
    numeros_usuario.append(int(numeros_del_usuario))
    numeros_del_usuario = ""
    print("Numero añadido")

numero_pequeno = numeros_usuario[0]
for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El numero menor es {}".format(numero_pequeno))

