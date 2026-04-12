"""
Juego de Contar Dinero — Crea un juego en el que el usuario debe ingresar la cantidad de monedas
necesarias para formar exactamente un dólar. El programa debe pedir la cantidad de pennies (1¢),
nickels (5¢), dimes (10¢) y quarters (25¢). Si el total es igual a un dólar, el programa debe
felicitar al usuario. De lo contrario, debe indicar si la cantidad ingresada fue mayor o menor
a un dólar.
"""

def juego_monedas():
    pennies = int(input("¿Cuántos pennies (1¢)? "))
    nickels = int(input("¿Cuántos nickels (5¢)? "))
    dimes = int(input("¿Cuántos dimes (10¢)? "))
    quarters = int(input("¿Cuántos quarters (25¢)? "))

    total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25

    if total == 100:
        print("¡Felicidades! ¡Formaste exactamente un dólar!")
    elif total > 100:
        print(f"Te pasaste. Ingresaste {total}¢, que es más de un dólar.")
    else:
        print(f"Faltaron monedas. Ingresaste {total}¢, que es menos de un dólar.")

def main():
    juego_monedas()

if __name__ == "__main__":
    main()
