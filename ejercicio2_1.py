# El código original de Java ha sido traducido a Python,
# manteniendo la estructura de clases y la funcionalidad.

class Persona:
    """
    Clase para representar a una persona con sus datos básicos.
    """

    def __init__(self, nombre, apellidos, numero_documento_identidad, anho_nacimiento):
        """
        Constructor de la clase Persona.

        Args:
            nombre (str): Nombre de la persona.
            apellidos (str): Apellidos de la persona.
            numero_documento_identidad (str): Número de documento de identidad.
            anho_nacimiento (int): Año de nacimiento.
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.anho_nacimiento = anho_nacimiento

    def imprimir(self):
        """
        Imprime los datos de la persona en la consola.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Número de documento de identidad: {self.numero_documento_identidad}")
        print(f"Año de nacimiento: {self.anho_nacimiento}")
        print("-" * 25)

def main():
    """
    Función principal para demostrar la creación y uso de objetos de la clase Persona.
    """
    # Creación de dos instancias de la clase Persona
    persona1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    persona2 = Persona("Luis", "León", "1053223344", 2001)

    # Llamada al método imprimir() para cada persona
    persona1.imprimir()
    persona2.imprimir()

if __name__ == "__main__":
    main()
