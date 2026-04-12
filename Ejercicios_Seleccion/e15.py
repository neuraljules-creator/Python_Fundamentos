"""
Calculadora de Tiempo — Escribe un programa que pida al usuario ingresar una cantidad
de segundos y funcione de la siguiente manera:
• Si los segundos son >= 60, mostrar la cantidad de minutos.
• Si los segundos son >= 3,600, mostrar la cantidad de horas.
• Si los segundos son >= 86,400, mostrar la cantidad de días.
"""

def calculadora_tiempo():
    segundos = int(input("Ingresa una cantidad de segundos: "))

    if segundos >= 86400:
        print(f"Días: {segundos // 86400}")
        print(f"Horas: {segundos // 3600}")
        print(f"Minutos: {segundos // 60}")
    elif segundos >= 3600:
        print(f"Horas: {segundos // 3600}")
        print(f"Minutos: {segundos // 60}")
    elif segundos >= 60:
        print(f"Minutos: {segundos // 60}")
    else:
        print(f"Segundos: {segundos}")

def main():
    calculadora_tiempo()

if __name__ == "__main__":
    main()
