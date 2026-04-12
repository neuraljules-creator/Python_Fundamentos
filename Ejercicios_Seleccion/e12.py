"""
Venta de Software — Una empresa vende un paquete a $99. Se aplican descuentos por cantidad:
• 10–19 unidades → 10% de descuento
• 20–49 unidades → 20% de descuento
• 50–99 unidades → 30% de descuento
• 100 o más unidades → 40% de descuento
Escribe un programa que pida al usuario la cantidad de paquetes comprados y muestre
el descuento aplicado y el total a pagar.
"""

def venta_software():
    cantidad = int(input("¿Cuántos paquetes deseas comprar? "))

    precio_unitario = 99

    if cantidad >= 100:
        descuento = 0.40
    elif cantidad >= 50:
        descuento = 0.30
    elif cantidad >= 20:
        descuento = 0.20
    elif cantidad >= 10:
        descuento = 0.10
    else:
        descuento = 0

    subtotal = cantidad * precio_unitario
    monto_descuento = subtotal * descuento
    total = subtotal - monto_descuento

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Descuento ({int(descuento * 100)}%): -${monto_descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")

def main():
    venta_software()

if __name__ == "__main__":
    main()
