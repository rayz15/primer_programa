numero_a_adivinar = int(input("¿que numero del 1 al 100 quieres que tu amigo adivine?"))
numero_elegido = int(input("Adivina el numero del 1 al 100 que tu amigo ha elegido"))

while int(input("Adivina el numero del 1 al 100 que tu amigo ha elegido")) != (numero_a_adivinar):
    if (numero_elegido != numero_a_adivinar):
        int(input("Adivina el numero del 1 al 100 que tu amigo ha elegido"))

print("Al fin lo adivinaste")
