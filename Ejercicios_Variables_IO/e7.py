# Starting Out with Python, Third Edition
# Capítulo 2, Ejercicio 6
"""
Write a program that will ask the user to enter the amount of a purchase. The program
should then compute the state and county sales tax. Assume the state sales tax is 5 percent
and the county sales tax is 2.5 percent. The program should display the amount of the purchase,
the state sales tax, the county sales tax, the total sales tax, and the total of the sale
(which is the sum of the amount of purchase plus the total sales tax).
Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
"""

def sales_tax():
    state_tax = 0.05
    county_tax  = 0.025
    amount = float(input("Enter the purchase amount: "))
    state_sales_tax = amount * state_tax
    county_sales_tax = amount * county_tax
    total_tax = amount * (state_tax + county_tax)
    sale_total = amount + total_tax
    print(f"total amount: ${amount:,.2f}")
    print(f"state tax: ${state_sales_tax:,.2f}")
    print(f"county tax: ${county_sales_tax:,.2f}")
    print(f"total tax: ${total_tax:,.2f}")
    print(f"total sale: ${sale_total:,.2f}")

def main():
    sales_tax()
    pass

if __name__ == "__main__":
    main()
