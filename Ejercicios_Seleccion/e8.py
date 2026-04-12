"""
Calculadora de Asado de Hot Dogs — Supón que los hot dogs vienen en paquetes de 10 y los panes
en paquetes de 8. Escribe un programa que calcule el número de paquetes de hot dogs y panes
necesarios para un asado, con la menor cantidad de sobrantes posible. El programa debe pedir
al usuario el número de personas y cuántos hot dogs recibirá cada una, y mostrar:
• El número mínimo de paquetes de hot dogs requeridos
• El número mínimo de paquetes de panes requeridos
• La cantidad de hot dogs que sobrarán
• La cantidad de panes que sobrarán
"""

import math

def calculadora_asado():
    personas = int(input("¿Cuántas personas asistirán al asado? "))
    hot_dogs_por_persona = int(input("¿Cuántos hot dogs recibirá cada persona? "))

    total_hot_dogs = personas * hot_dogs_por_persona

    paquetes_hot_dogs = math.ceil(total_hot_dogs / 10)
    paquetes_panes = math.ceil(total_hot_dogs / 8)

    sobrantes_hot_dogs = (paquetes_hot_dogs * 10) - total_hot_dogs
    sobrantes_panes = (paquetes_panes * 8) - total_hot_dogs

    print(f"\nPaquetes de hot dogs necesarios: {paquetes_hot_dogs}")
    print(f"Paquetes de panes necesarios: {paquetes_panes}")
    print(f"Hot dogs sobrantes: {sobrantes_hot_dogs}")
    print(f"Panes sobrantes: {sobrantes_panes}")

def main():
    calculadora_asado()

if __name__ == "__main__":
    main()
