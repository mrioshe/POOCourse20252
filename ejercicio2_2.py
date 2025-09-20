from enum import Enum

class tipoPlaneta(Enum):
    """
    Representa el tipo de planeta.
    """
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    """
    Clase que representa un planeta en el sistema solar.
    """
    
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable):
        """
        Constructor de la clase Planeta.

        Args:
            nombre (str): Nombre del planeta.
            cantidad_satelites (int): Número de satélites naturales.
            masa (float): Masa del planeta en kg.
            volumen (float): Volumen del planeta en km^3.
            diametro (int): Diámetro del planeta en km.
            distancia_sol (int): Distancia al Sol en km.
            tipo (tipoPlaneta): Tipo de planeta.
            es_observable (bool): Si es observable o no.
        """
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        """
        Imprime las propiedades del planeta.
        """
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa} kg")
        print(f"Volumen del planeta = {self.volumen} km^3")
        print(f"Diámetro del planeta = {self.diametro} km")
        print(f"Distancia al sol = {self.distancia_sol} km")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")
        
    def calcular_densidad(self):
        """
        Calcula y devuelve la densidad del planeta.
        """
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        """
        Determina si el planeta es exterior (distancia al sol > 3.4 UA).
        Una unidad astronómica (UA) es aproximadamente 149,597,870 km.
        
        Returns:
            bool: True si es un planeta exterior, False en caso contrario.
        """
        limite_ua = 149597870 * 3.4
        return self.distancia_sol > limite_ua

def main():
    """
    Función principal para demostrar el uso de la clase Planeta.
    """
    # Creación del primer planeta: Tierra
    p1 = Planeta("Tierra", 1, 5.9736e24, 1.0832e12, 12742, 150000000, tipoPlaneta.TERRESTRE, True)
    p1.imprimir()
    print(f"Densidad del planeta = {p1.calcular_densidad():.2e} kg/km^3")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
    print("-" * 20)
    
    # Creación del segundo planeta: Júpiter
    p2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 13820, 750000000, tipoPlaneta.GASEOSO, True)
    p2.imprimir()
    print(f"Densidad del planeta = {p2.calcular_densidad():.2e} kg/km^3")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}")

if __name__ == "__main__":
    main()
