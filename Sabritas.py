quieres_sabritas = input ( "quieres sabrtias? (si/no): ")
tienes_dinero = input ("tienes dinero suficiente? (si/no):")
sabritas_de_limon = input ("hay sabritas de limon? (si/no):")
esta_mama = input ("estas con mama? (si/no):")

if quieres_sabritas == "si" and (tienes_dinero == "si"  or esta_mama == "si") and sabritas_de_limon == "si":
    print("compra entonces")
else:
    print ("entonces nada")