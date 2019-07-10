pokemon_elegido = input("¿contra que pokemon quieres luchar (Ratata / Pidgeon / Miau): ")

vida_charmander = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "Ratata":
    vida_enemigo = 70
    nombre_pokemon = "Ratata"
    ataque_pokemon = 8
elif pokemon_elegido == "Pidgeon":
    vida_enemigo = 90
    nombre_pokemon = "Pidgeon"
    ataque_pokemon = 11
elif pokemon_elegido == "Miau":
    vida_enemigo = 130
    nombre_pokemon = "Miau"
    ataque_pokemon = 14

while vida_charmander > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿que ataque quieres usar? ( Lanzallamas / Coletazo ): ")
    if ataque_elegido == "Lanzallamas":
        vida_enemigo -= 15
    if ataque_elegido == "Coletazo":
        vida_enemigo -=10

    print("La vida de {} es {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace daño de {} puntos".format(nombre_pokemon, ataque_pokemon))
    vida_charmander -= ataque_pokemon

    print("La vida de Charmander es {}".format(vida_charmander))


if vida_enemigo <=0:
    print("Charmander ha ganado")
if vida_charmander <= 0:
    print("Charmander ha sido derrotado")
print("Fin del combate")

