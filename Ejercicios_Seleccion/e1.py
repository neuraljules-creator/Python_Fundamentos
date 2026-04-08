"""
Día de la Semana — Escribe un programa que le pida al usuario un número del 1 al 7.
 El programa debe mostrar el día de la semana correspondiente, donde 1 = Lunes, 2 = Martes, 3 = Miércoles, 4 = Jueves, 5 = Viernes, 6 = Sábado y 7 = Domingo. 
El programa debe mostrar un mensaje de error si el usuario ingresa un número fuera del rango de 1 a 7. 
"""

def dia_de_semana():
    numero_dia = int(input("Ingrese un numero del 1 al 7: "))
    if numero_dia == 1:
        print("El dia es Lunes")
    elif numero_dia == 2:
        print("El dia es martes")
    elif numero_dia == 3:
        print("El dia es miercoles")
    elif numero_dia == 4:
        print("El dia es jueves")
    elif numero_dia == 5:
        print("El dia es Viernes")
    elif numero_dia == 6:
        print("El dia es Sabado")
    elif numero_dia == 7:
        print("El dia es Domingo")
    else:
        print("Numero Invalido")

def main():
    dia_de_semana()
    pass

if __name__ == "__main__":
    main()