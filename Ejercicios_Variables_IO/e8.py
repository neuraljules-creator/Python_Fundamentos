# Starting Out with Python, Third Edition
# Capítulo 2, Ejercicio 8

"""
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, and then calculate the amount
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
"""

def tip_tax_total():
    tip = 0.18
    sales_tax = 0.07

    food_amount = float(input("Enter the amount for the food: "))
    tip_amount = food_amount * tip
    sales_tax_amount = food_amount * sales_tax
    total = food_amount + tip_amount + sales_tax_amount
    print(f"Propina: ${tip_amount:,.2f}")
    print(f"tax amount: ${sales_tax_amount:,.2f}")
    print(f"Total: ${total:,.2f}")


def main():
    tip_tax_total()
    pass

if __name__ == "__main__":
    main()
