import math

class Calculos:
    """A class to perform specific mathematical calculations."""
    @staticmethod
    def calcular_suma(suma, x):
        """Calculates the sum of two numbers."""
        return suma + x

    @staticmethod
    def calcular_x(x, y):
        """Calculates x based on y squared and x."""
        return math.pow(y, 2) + x

def main():
    """Main function to handle user input and perform calculations."""
    print("Ingresa un número para la suma:")
    try:
        suma = float(input())
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return

    print("Ingresa un número para x:")
    try:
        x = float(input())
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return

    print("Ingresa un número para y:")
    try:
        y = float(input())
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return

    if y == 0:
        print("Error: No se puede dividir por cero.")
        return

    # Create an instance of the Calculos class to use its methods
    calculos = Calculos()

    # Perform the calculations
    suma = calculos.calcular_suma(suma, x)
    x = calculos.calcular_x(x, y)
    
    # Final calculation and output
    suma = suma + (x / y)

    print(f"El valor de la suma es: {suma}")

if __name__ == "__main__":
    main()