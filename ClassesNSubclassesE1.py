# Clase padre
class Vehicle:
    def __init__(self):
        self.brand = "Ford"

    def honk(self):
        print("tuut, tiit!")


# Clase hija
class Car(Vehicle):
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase padre
        self.modelName = "Mustang"


# Programa principal
if __name__ == "__main__":
    print("Prueba de clase y subclase!!")

    myCar = Car()

    # Atributo heredado
    print(myCar.brand)

    # Método heredado
    myCar.honk()

    # Atributo propio de la clase Car
    print(myCar.modelName)