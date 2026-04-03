"""
3. Calcular Terreno
Un acre de terreno equivale a 43560 pies cuadrados. Escribe un programa que pide al usuario ingresar el total de pies cuadrados en un terreno, y calcula el numero de acres en el terreno. 

"""


def calcular_terreno():
    acre = 43560
    total_pies_cuadrados = float(input("Ingresa el total de pies cuadrados: "))
    numero_acres = total_pies_cuadrados / acre
    # Con f string
    print(f"Equivale a: {numero_acres:.2f} acres")

def main():
    # Llamadas
    calcular_terreno()
    pass

if __name__ == "__main__":
    main()

