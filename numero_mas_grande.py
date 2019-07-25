numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(float(numero_del_usuario))
    numero_del_usuario = ""
    print("Numero añadido")

print(numeros_usuario)
media = (numeros_usuario [0] + numeros_usuario [1] + numeros_usuario [2] + numeros_usuario [3] + numeros_usuario [4] + numeros_usuario [5] + numeros_usuario [6] + numeros_usuario [7] + numeros_usuario [8] + numeros_usuario [9]) / 10
print(media)
