"""
5. Distancia recorrida
La distancia que viaja un auto en línea recta se puede calcular como:                Distancia = Velocidad X Tiempo
Un auto viaja a 70 millas por hora, escribe un programa que imprima lo siguiente:
a.	La distancia recorrida en 6 horas
b.	La distancia recorrida en 10 horas
c.	La distancia recorrida en 15 horas
"""

def distancia_recorrida():
    velocidad = 70.0 #millas por hora
    distancia1 = velocidad * 6
    distancia2 = velocidad * 10
    distancia3 = velocidad * 15
    print(f"Distancia recorrida en 6 horas: {distancia1:.2f} millas")
    print(f"Distancia recorrida en 10 horas: {distancia2:.2f} millas")
    print(f"Distancia recorrida en 15 horas: {distancia3:.2f} millas")

def main():
    distancia_recorrida()
    pass

if __name__ == "__main__":
    main()