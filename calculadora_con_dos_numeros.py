
operacion= input("¿Que operacion deseas realizar? (Suma / Resta / Multiplicacion / Division): ")
primer_numero = float(input("Escribe el primer numero que deseas utilizar "))
segundo_numero = float(input("Escribe el segundoo numero que deseas utilizar "))
resultado = 0
if operacion == "Suma":
   resultado =  (primer_numero + segundo_numero)

elif operacion == "Resta":
    resultado = (primer_numero - segundo_numero)

elif operacion == "Multiplicacion":
    resultado = (primer_numero * segundo_numero)

elif operacion == "Division":
    resultado = (primer_numero / segundo_numero)

else:
    print("Escibiste mal la operacion")

print(resultado)
print("Fin del programa")
