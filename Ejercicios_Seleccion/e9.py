"""
Colores de la Ruleta — En una ruleta, los bolsillos están numerados del 0 al 36. Los colores son:
• El bolsillo 0 es verde.
• Del 1 al 10: los impares son rojos y los pares son negros.
• Del 11 al 18: los impares son negros y los pares son rojos.
• Del 19 al 28: los impares son rojos y los pares son negros.
• Del 29 al 36: los impares son negros y los pares son rojos.
Escribe un programa que pida al usuario un número de bolsillo y muestre si es verde, rojo o negro.
Si el número está fuera del rango 0-36, debe mostrar un mensaje de error.
"""

def color_ruleta():
    numero = int(input("Ingresa un número de bolsillo (0-36): "))

    if numero < 0 or numero > 36:
        print("Error: el número debe estar entre 0 y 36.")
    elif numero == 0:
        print("El bolsillo es verde.")
    elif 1 <= numero <= 10 or 19 <= numero <= 28:
        if numero % 2 != 0:
            print("El bolsillo es rojo.")
        else:
            print("El bolsillo es negro.")
    else:
        if numero % 2 != 0:
            print("El bolsillo es negro.")
        else:
            print("El bolsillo es rojo.")

def main():
    color_ruleta()

if __name__ == "__main__":
    main()
