"""
Masa y Peso — Los científicos miden la masa de un objeto en kilogramos y su peso en newtons. Si conoces la masa en kilogramos, puedes calcular el peso con la fórmula: 
peso = masa × 9.8. Escribe un programa que pida la masa de un objeto y calcule su peso. 
Si pesa más de 500 newtons, debe mostrar un mensaje indicando que es muy pesado. Si pesa menos de 100 newtons, debe mostrar que es muy ligero. 
"""

def MasaYPeso():
    # Entrada de datos
    masa = float(input("Ingrese la masa del objeto: "))

    # Calculo
    peso = masa * 9.8

    if peso > 500:
        print("Objeto mas pesado")
    elif peso < 100:
        print("Muy ligero")
    else:
        print("Dentro de rango")
    pass

def main():
    MasaYPeso()

if __name__ == "__main__":
    main()

