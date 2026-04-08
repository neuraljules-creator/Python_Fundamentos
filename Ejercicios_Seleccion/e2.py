"""
 Áreas de Rectángulos — El área de un rectángulo es su largo por su ancho. 
 Escribe un programa que pida el largo y el ancho de dos rectángulos. 
 El programa debe indicarle al usuario cuál rectángulo tiene mayor área, o si las áreas son iguales. 
"""

def area_rectangulo():
    largo1 = float(input("Ingresa el largo del primer rectangulo: "))
    ancho1 = float(input("Ingresa el ancho del primer rectangulo: "))
    largo2 = float(input("Ingresa el largo del segundo rectangulo: "))
    ancho2 = float(input("Ingresa el ancho del segundo rectangulo: "))

    area1 = largo1 * ancho1
    area2 = largo2 * ancho2

    if area1 > area2:
        print("Primer Rectangulo es mayor")
    elif area2 > area1:
        print("Segundo Rectangulo es mayor")
    else:
        print("Los dos rectangulos son iguales")
    pass 

def main():
    area_rectangulo()

if __name__ == "__main__":
    main()