frase_usuario = input("Escribe una frase que contenga puntos y comas: ")
espacios = " "
puntos = "."
comas = ","

num_espacios = 0
num_puntos = 0
num_comas = 0

for signo in frase_usuario:
    if signo in espacios:
        num_espacios += 1
    if signo in puntos:
        num_puntos += 1
    if signo in comas:
        num_comas += 1

print("Hay {} espacios".format(num_espacios))
print("Hay {} puntos".format(num_puntos))
print("Hay {} comas".format(num_comas))


