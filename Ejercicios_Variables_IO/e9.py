# Starting Out with Python, Third Edition
# Capítulo 2, Ejercicio 9

"""
Write a program that converts Celsius temperatures to Fahrenheit temperatures.
"""

def celsius_to_fahrenheit():
    celsius = float(input("Enter the temp in celsius: "))
    Fahrenheit = (9/5)*celsius + 32
    print(f"The temp in F°: {Fahrenheit:,.2f} F°")

def main():
    celsius_to_fahrenheit()
    pass

if __name__ == "__main__":
    main()
