pokemon_elegido = input("¿contra que pokemon quieres luchar (Ratata / Pidgeon / Miau): ")

vida_charmander = 100
vida_enemigo = 0

if pokemon_elegido == "Ratata":
    vida_enemigo = 70
if pokemon_elegido == "Pidgeon":
    vida_enemigo = 90
if pokemon_elegido == "Miau":
    vida_enemigo = 130

while vida_charmander > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿que ataque quieres usar? ( Lanzallamas / Coletazo ): ")
    if ataque_elegido == "Lanzallamas":
        vida_enemigo -= 15
    if ataque_elegido == "Coletazo":
        vida_enemigo -=10

    print("La vida del enemigo es {}".format(vida_enemigo))

    if pokemon_elegido == "Ratata":
        print("Ratata te hace 8 de daño")
        vida_charmander -= 8
    if pokemon_elegido == "Pidgeon":
        print("Pidgeon te hace 11 de daño")
        vida_charmander -= 11
    if pokemon_elegido == "Miau":
        print("Miau te hace 14 de daño")
        vida_charmander -= 14

    print("La vida de Charmander es {}".format(vida_charmander))


if vida_enemigo <=0:
    print("Charmander ha ganado")
if vida_charmander <= 0:
    print("Charmander ha sido derrotado")
print("Fin del combate")

