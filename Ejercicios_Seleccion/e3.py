"""
Clasificador de Edad — Escribe un programa que le pida al usuario ingresar la edad de una persona. 
El programa debe mostrar un mensaje indicando si la persona es un bebé, un niño, un adolescente o un adulto, según estas reglas: si tiene 1 año o menos es bebé,
 si tiene más de 1 pero menos de 13 es niño, si tiene al menos 13 pero menos de 20 es adolescente, si tiene 20 o más es adulto. 
"""

def clasificador_edad():
    edad = float(input("Ingrese la edad: "))
    if edad <= 1:
        print("Es un Infante")
    elif edad < 13:
        print("Es un Niño")
    elif edad < 20:
        print("Es un adolescente")
    else:
        print("Es un adulto")
    pass

def main():
    clasificador_edad()

if __name__ == "__main__":
    main()