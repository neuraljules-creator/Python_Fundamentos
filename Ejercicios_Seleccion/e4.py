"""
Números Romanos — Escribe un programa que le pida al usuario ingresar un número del 1 al 10. El programa debe mostrar la versión en número romano. 
Si el número está fuera del rango de 1 a 10, debe mostrar un mensaje de error. La tabla es: 1=I, 2=II, 3=III, 4=IV, 5=V, 6=VI, 7=VII, 8=VIII, 9=IX, 10=X. 
"""

def numeros_romanos():
    numero_dia = int(input("Ingrese un numero del 1 al 10: "))
    if numero_dia == 1:
        print("I")
    elif numero_dia == 2:
        print("II")
    elif numero_dia == 3:
        print("III")
    elif numero_dia == 4:
        print("IV")
    elif numero_dia == 5:
        print("V")
    elif numero_dia == 6:
        print("VI")
    elif numero_dia == 7:
        print("VII")
    elif numero_dia == 8:
        print("VIII")
    elif numero_dia == 9:
        print("IX")
    elif numero_dia == 10:
        print("X")
    else:
        print("Numero Invalido")

def main():
    numeros_romanos()
    pass

if __name__ == "__main__":
    main()