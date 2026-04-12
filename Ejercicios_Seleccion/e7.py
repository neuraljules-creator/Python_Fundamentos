"""
Mezclador de Colores — Los colores rojo, azul y amarillo se conocen como colores primarios porque no pueden
obtenerse mezclando otros colores. Cuando mezclas dos colores primarios, obtienes un color secundario:
al mezclar rojo y azul obtienes morado, rojo y amarillo obtienes naranja, azul y amarillo obtienes verde.
Diseña un programa que le pida al usuario ingresar los nombres de dos colores primarios para mezclar.
Si el usuario ingresa algo distinto a "rojo", "azul" o "amarillo", el programa debe mostrar un mensaje
de error. De lo contrario, debe mostrar el nombre del color secundario resultante.
"""

def mezclador():
    color1 = input("Ingresa el primer color primario: ").lower()
    color2 = input("Ingresa el segundo color primario: ").lower()

    primarios = ["rojo", "azul", "amarillo"]

    if color1 not in primarios:
        print(f"Error: '{color1}' no es un color primario.")
    elif color2 not in primarios:
        print(f"Error: '{color2}' no es un color primario.")
    elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        print("Al mezclar rojo y azul obtienes: morado")
    elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
        print("Al mezclar rojo y amarillo obtienes: naranja")
    elif (color1 == "azul" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "azul"):
        print("Al mezclar azul y amarillo obtienes: verde")
    else:
        print("No puedes mezclar el mismo color.")

def main():
    mezclador()

if __name__ == "__main__":
    main()
