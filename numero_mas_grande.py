numeros_usuario = []
numeros_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numeros_del_usuario.isdigit():
        numeros_del_usuario = input("Escribe un numero: ")
    numeros_usuario.append(int(numeros_del_usuario))
    numeros_del_usuario = ""
    print("Numero añadido")

numero_grande = numeros_usuario[0]
for numero in numeros_usuario:
    if numero > numero_grande:
        numero_grande = numero

print("El numero mayor es {}".format(numero_grande))

