quieres_cine_input = input("¿quieres ir al cine? (Si/No): ").upper()
tienes_dinero_input = input("¿Tienes dinero para pagar la entrada? (Si/No):").upper()
vas_solo_input = input("¿vas solito? (Si/No):").upper()

quieres_cine = quieres_cine_input
tienes_dinero = tienes_dinero_input
vas_solo = vas_solo_input

if quieres_cine == "SI" and tienes_dinero == "SI":
    print("No lo pienses mas, ve al cine")
if quieres_cine == "NO":
    print("Entonces no me estes molestando si no queres ir")
if tienes_dinero == "NO":
    print("no puedes ir sin dinero por mas gans que tengas")
if vas_solo_input == "SI":
    print("...y ve pero sin llorar")


