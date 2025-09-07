import math

class Calculos:
    """A class containing static methods for mathematical calculations."""

    @staticmethod
    def calcular_cuadrado(numero):
        """Calculates the square of a number."""
        return math.pow(numero, 2)

    @staticmethod
    def calcular_cubo(numero):
        """Calculates the cube of a number."""
        return math.pow(numero, 3)

def main():
    """Main function to prompt for a number and print its square and cube."""
    try:
        numero = float(input("Ingresa el número: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return

    numero_cuadrado = Calculos.calcular_cuadrado(numero)
    numero_cubico = Calculos.calcular_cubo(numero)
    
    print(f"\nNúmero al cuadrado: {numero_cuadrado}")
    print(f"Número al cubo: {numero_cubico}")

if __name__ == "__main__":
    main()