import math

class Circulo:
    """Clase para representar un círculo."""

    def __init__(self, radio):
        """Constructor de la clase Círculo."""
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * math.pow(self.radio, 2)
    
    def calcular_perimetro(self):
        """Calcula el perímetro del círculo."""
        return 2 * math.pi * self.radio

class Cuadrado:
    """Clase para representar un cuadrado."""

    def __init__(self, lado):
        """Constructor de la clase Cuadrado."""
        self.lado = lado

    def calcular_area(self):
        """Calcula el área del cuadrado."""
        # Se ha corregido la lógica del código original.
        return self.lado * self.lado

    def calcular_perimetro(self):
        """Calcula el perímetro del cuadrado."""
        # Se ha corregido la lógica del código original.
        return 4 * self.lado

class Rectangulo:
    """Clase para representar un rectángulo."""

    def __init__(self, base, altura):
        """Constructor de la clase Rectángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * self.base + 2 * self.altura

class TrianguloRectangulo:
    """Clase para representar un triángulo rectángulo."""

    def __init__(self, base, altura):
        """Constructor de la clase Triángulo Rectángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2
    
    def calcular_hipotenusa(self):
        """Calcula la hipotenusa del triángulo."""
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self):
        """Calcula el perímetro del triángulo."""
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        """Determina el tipo de triángulo (isósceles o escaleno)."""
        # Se ha corregido la lógica del código original.
        # Un triángulo rectángulo no puede ser equilátero.
        if self.base == self.altura:
            print("Es un triángulo isósceles")
        else:
            print("Es un triángulo escaleno")

def main():
    """
    Función principal para demostrar las clases de figuras geométricas.
    """
    circulo = Circulo(2)
    rectangulo = Rectangulo(1, 2)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 5)

    print(f"El área del círculo es = {circulo.calcular_area()}")
    print(f"El perímetro del círculo es = {circulo.calcular_perimetro()}")
    print()
    print(f"El área del rectángulo es = {rectangulo.calcular_area()}")
    print(f"El perímetro del rectángulo es = {rectangulo.calcular_perimetro()}")
    print()
    print(f"El área del cuadrado es = {cuadrado.calcular_area()}")
    print(f"El perímetro del cuadrado es = {cuadrado.calcular_perimetro()}")
    print()
    print(f"El área del triángulo es = {triangulo.calcular_area()}")
    print(f"El perímetro del triángulo es = {triangulo.calcular_perimetro()}")
    triangulo.determinar_tipo_triangulo()

if __name__ == "__main__":
    main()
