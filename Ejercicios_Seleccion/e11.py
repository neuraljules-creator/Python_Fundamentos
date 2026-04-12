"""
Puntos del Club de Libros — Serendipity Booksellers tiene un club que otorga puntos según
la cantidad de libros comprados cada mes:
• 0 libros → 0 puntos
• 2 libros → 5 puntos
• 4 libros → 15 puntos
• 6 libros → 30 puntos
• 8 o más libros → 60 puntos
Escribe un programa que pida al usuario la cantidad de libros comprados este mes
y muestre los puntos obtenidos.
"""

def puntos_club():
    libros = int(input("¿Cuántos libros compraste este mes? "))

    if libros == 0:
        puntos = 0
    elif libros < 4:
        puntos = 5
    elif libros < 6:
        puntos = 15
    elif libros < 8:
        puntos = 30
    else:
        puntos = 60

    print(f"Puntos obtenidos: {puntos}")

def main():
    puntos_club()

if __name__ == "__main__":
    main()
