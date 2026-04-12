"""
•  Fechas Mágicas — La fecha 10 de junio de 1960 es especial porque escrita como 6/10/60, el mes por el día es igual al año.
 Escribe un programa que pida al usuario un mes (en número), un día y un año de dos dígitos. 
El programa debe determinar si el mes multiplicado por el día es igual al año. Si es así, debe mostrar que la fecha es mágica; de lo contrario, que no lo es.
"""

def fecha_magica():
    mes, dia, año = input("Ingrese el mes, día y año (en formato MM/DD/AA): ").split("/")
    mes = int(mes)
    dia = int(dia)
    año = int(año)
    if mes * dia == año:
        print("La fecha es mágica.")
    else:
        print("La fecha no es mágica.")

def main():
    fecha_magica()
    pass

if __name__ == "__main__":
    main()