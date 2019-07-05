quieres_sabritas_input = input ( "quieres sabrtias de limon? (si/no): ")
if quieres_sabritas_input == "si":
    quieres_sabritas = True
elif quieres_sabritas_input == "no":
    quieres_sabritas = False
else:
    print("tienes que decir que si on no sucio mortal")
    quieres_sabritas = False

tienes_dinero_input = input ("tienes dinero suficiente? (si/no):")
sabritas_de_limon_input = input ("hay sabritas de limon? (si/no):")
esta_mama_input = input ("estas con mama? (si/no):")

quieres_sabritas = quieres_sabritas_input == "si"
puedes_comprar = tienes_dinero_input == "si" or esta_mama_input == "si"
hay_sabritas_limon = sabritas_de_limon_input == "si"

if quieres_sabritas and puedes_comprar and hay_sabritas_limon:
    print("compra entonces")
else:
    print ("entonces nada")