"""
4. Compra total
Un Cliente compra en una tienda 5 items. Escribe un programa que pida al usuario el precio de cada item e imprima el subtotal de la venta,
 el monto de los impuestos de venta, y el total. Asume que el impuesto de venta es del 7 por ciento.
"""


def compra_total():
    impuesto_venta = 0.07
    item1, item2, item3, item4, item5 = input("Ingrese el precio de cada item seguido por un espacio: ").split(",") # Separar la entrada por espacios
    item1 = float(item1)
    item2 = float(item2)
    item3 = float(item3)
    item4 = float(item4)
    item5 = float(item5)
    subtotal = item1 + item2 + item3 + item4 + item5
    print(f"Subtotal: ${subtotal:.2f} ")
    print(f"Impuesto de venta: ${(subtotal * impuesto_venta):.2f}")
    print(f"Total: {(subtotal * 1.07):.2f}")


def main():
    compra_total()
    pass

if __name__ == "__main__":
    main()
