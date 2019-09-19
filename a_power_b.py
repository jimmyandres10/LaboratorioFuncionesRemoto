base= int(input("de la base del numero "))
expo= int(input("de el exponente del numero "))

def a_power_b(base,expo):
    potencia=1
    if base != 0:

        for i in range (1,expo+1):
            potencia=potencia*expo
            print ()
    else:

        print("su valor cero no es aceptable")

        return potencia

x=a_power_b(base,expo)
if base!=0 :
    print(f"su valor es {x}")


