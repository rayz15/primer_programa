frase_usuario = input("Escribe una frase y no olvides usar mayusculas: ")

mayusculas = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J","K","L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

num_mayusculas = 0

for letra in frase_usuario:
    if letra in mayusculas:
        num_mayusculas += 1

print("Hay {} Mayuculas en tu texto".format(num_mayusculas))