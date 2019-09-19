base= int(input("de la base del numero "))
expo= int(input("de el exponente del numero "))

def a_power_b(base,expo):
    potencia=1
    for i in range (1,expo+1):
        potencia=potencia*expo
        print ()

    return potencia

x=a_power_b(base,expo)
print(f"su valor es {x}")