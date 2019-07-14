frase_usuario = input("Escibe cualquier frase: ")

vocales = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]

for letra in frase_usuario:
    if letra in vocales:
        print("{}".format(letra))