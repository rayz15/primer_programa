num_tabla = int(input("Escibe el numero del que quieres ver su tabla de multiplicar hasta el 10: "))

for multiplo in range(5, 16):
    print("{} x {} = {}".format(num_tabla, multiplo, num_tabla * multiplo))

