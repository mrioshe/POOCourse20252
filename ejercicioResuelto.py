import math

class Calculos:
    """A class containing static methods to calculate properties of a circle."""

    @staticmethod
    def calcular_longitud_circulo(radio):
        """
        Calculates the circumference of a circle given its radius.
        
        Args:
            radio (float): The radius of the circle.
            
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * radio

    @staticmethod
    def calcular_area_circulo(radio):
        """
        Calculates the area of a circle given its radius.
        
        Args:
            radio (float): The radius of the circle.
            
        Returns:
            float: The area of the circle.
        """
        return math.pi * math.pow(radio, 2)

class EjercicioResuelto17:
    """
    Main class to prompt for user input and display the circumference and area of a circle.
    """
    @staticmethod
    def main():
        """
        Main method to execute the program.
        """
        try:
            radio = float(input("Ingresa el radio: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
            return

        longitud_circunferencia = Calculos.calcular_longitud_circulo(radio)
        area_circunferencia = Calculos.calcular_area_circulo(radio)

        print(f"\nLongitud circunferencia: {longitud_circunferencia}")
        print(f"Área circunferencia: {area_circunferencia}")

if __name__ == "__main__":
    EjercicioResuelto17.main()