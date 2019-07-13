mi_lista = ["Pan", "Queso", "Jamon Serrano", "Zanahoria", "Carne", "Pollo", "Huevos"]

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de las compras")