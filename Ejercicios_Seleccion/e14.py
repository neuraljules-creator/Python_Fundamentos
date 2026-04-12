"""
Índice de Masa Corporal (IMC) — El IMC se utiliza para determinar si una persona tiene
sobrepeso o bajo peso en relación a su estatura. La fórmula es:
IMC = peso × 703 / estatura²
donde el peso se mide en libras y la estatura en pulgadas. El programa debe pedir al
usuario su peso y estatura, calcular el IMC y mostrar si tiene:
• Peso óptimo: IMC entre 18.5 y 25
• Bajo peso: IMC menor a 18.5
• Sobrepeso: IMC mayor a 25
"""

def calcular_imc():
    peso = float(input("Ingresa tu peso (en libras): "))
    estatura = float(input("Ingresa tu estatura (en pulgadas): "))

    imc = peso * 703 / estatura ** 2

    print(f"\nTu IMC es: {imc:.2f}")

    if imc < 18.5:
        print("Clasificación: Bajo peso.")
    elif imc <= 25:
        print("Clasificación: Peso óptimo.")
    else:
        print("Clasificación: Sobrepeso.")

def main():
    calcular_imc()

if __name__ == "__main__":
    main()
