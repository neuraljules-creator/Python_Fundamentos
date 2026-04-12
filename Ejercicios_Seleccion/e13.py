"""
Cargos de Envío — La empresa Fast Freight cobra las siguientes tarifas según el peso del paquete:
• 2 libras o menos → $1.50 por libra
• Más de 2 hasta 6 libras → $3.00 por libra
• Más de 6 hasta 10 libras → $4.00 por libra
• Más de 10 libras → $4.75 por libra
Escribe un programa que pida al usuario el peso del paquete y muestre el costo de envío.
"""

def cargos_envio():
    peso = float(input("Ingresa el peso del paquete (en libras): "))

    if peso <= 2:
        tarifa = 1.50
    elif peso <= 6:
        tarifa = 3.00
    elif peso <= 10:
        tarifa = 4.00
    else:
        tarifa = 4.75

    costo = peso * tarifa
    print(f"Costo de envío: ${costo:.2f}")

def main():
    cargos_envio()

if __name__ == "__main__":
    main()
