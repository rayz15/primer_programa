num_tabla = int(input("Escibe el numero del que quieres ver su tabla de multiplicar hasta el 10: "))
for multiplo in range(1, 16):
    if  multiplo % 2 == 0:
        print("{} x {} = {}".format(num_tabla, multiplo, num_tabla * multiplo))

