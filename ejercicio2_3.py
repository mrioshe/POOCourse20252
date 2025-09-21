from enum import Enum

class tipoCom(Enum):
    """Tipos de combustible para un automóvil."""
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diesel"
    BIODISEL = "Biodiesel"
    GAS_NATURAL = "Gas Natural"

class tipoA(Enum):
    """Tipos de carrocería de un automóvil."""
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class tipoColor(Enum):
    """Colores de un automóvil."""
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    """Clase que representa un automóvil y sus propiedades."""

    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color):
        """
        Constructor de la clase Automovil.

        Args:
            marca (str): Marca del automóvil.
            modelo (int): Modelo del año.
            motor (int): Capacidad del motor.
            tipo_combustible (tipoCom): Tipo de combustible.
            tipo_automovil (tipoA): Tipo de carrocería.
            numero_puertas (int): Número de puertas.
            cantidad_asientos (int): Cantidad de asientos.
            velocidad_maxima (int): Velocidad máxima en km/h.
            color (tipoColor): Color del automóvil.
        """
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0  # Inicializamos la velocidad actual en 0

    def get_velocidad_actual(self):
        """Obtiene la velocidad actual del automóvil."""
        return self.velocidad_actual

    def set_velocidad_actual(self, velocidad):
        """Establece la velocidad actual del automóvil."""
        self.velocidad_actual = velocidad

    def acelerar(self, incremento_velocidad):
        """Aumenta la velocidad del automóvil, si no excede la velocidad máxima."""
        nueva_velocidad = self.velocidad_actual + incremento_velocidad
        if nueva_velocidad <= self.velocidad_maxima:
            self.velocidad_actual = nueva_velocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def desacelerar(self, decremento_velocidad):
        """Disminuye la velocidad del automóvil, si no se vuelve negativa."""
        nueva_velocidad = self.velocidad_actual - decremento_velocidad
        if nueva_velocidad >= 0:
            self.velocidad_actual = nueva_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        """Detiene el automóvil, estableciendo la velocidad actual a 0."""
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        """Calcula el tiempo estimado de llegada a una distancia dada."""
        if self.velocidad_actual > 0:
            return distancia / self.velocidad_actual
        else:
            print("El automóvil no se está moviendo. No se puede calcular el tiempo.")
            return -1

    def imprimir(self):
        """Imprime todas las propiedades del automóvil."""
        print("-" * 25)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor}")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Cantidad de asientos: {self.cantidad_asientos}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print("-" * 25)

def main():
    """Función principal que ejecuta la lógica del programa."""
    auto1 = Automovil("Ford", 2018, 3, tipoCom.DIESEL, tipoA.EJECUTIVO, 5, 6, 250, tipoColor.NEGRO)
    
    auto1.imprimir()
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual: {auto1.velocidad_actual} km/h")
    auto1.acelerar(20)
    print(f"Velocidad actual después de acelerar: {auto1.velocidad_actual} km/h")
    auto1.desacelerar(50)
    print(f"Velocidad actual después de desacelerar: {auto1.velocidad_actual} km/h")
    auto1.frenar()
    print(f"Velocidad actual después de frenar: {auto1.velocidad_actual} km/h")
    auto1.desacelerar(20)

if __name__ == "__main__":
    main()
