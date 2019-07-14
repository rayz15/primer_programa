frase_usuario = input("Escibe alguna frase: ")
vocales = ["a", "i", "u", "e", "o"]

num_vocales = 0
num_consonates = 0

for letra in frase_usuario:
    if letra in vocales:
        num_vocales += 1
    else:
        num_consonates += 1

print("Hay {} vocales".format(num_vocales))
print("Hay {} consonantes".format(num_consonates))
