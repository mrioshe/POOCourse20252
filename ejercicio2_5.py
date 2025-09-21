from enum import Enum

class tipo(Enum):
    """
    Representa los tipos de cuenta bancaria.
    """
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.
    """
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            nombres_titular (str): Los nombres del titular de la cuenta.
            apellidos_titular (str): Los apellidos del titular de la cuenta.
            numero_cuenta (int): El número de la cuenta.
            tipo_cuenta (tipo): El tipo de cuenta (Ahorros o Corriente).
        """
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        """
        Imprime la información completa de la cuenta bancaria.
        """
        print("-" * 30)
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.value}")
        print(f"Saldo actual = ${self.saldo:.2f}")
        print("-" * 30)

    def consultar_saldo(self):
        """
        Imprime el saldo actual de la cuenta.
        """
        print(f"El saldo actual es = ${self.saldo:.2f}")

    def consignar(self, valor):
        """
        Consigna (deposita) un valor en la cuenta.
        
        Args:
            valor (float): El monto a consignar.
            
        Returns:
            bool: True si la transacción fue exitosa, False en caso contrario.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:.2f} en la cuenta. El nuevo saldo es ${self.saldo:.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        """
        Retira un valor de la cuenta.
        
        Args:
            valor (float): El monto a retirar.
            
        Returns:
            bool: True si la transacción fue exitosa, False en caso contrario.
        """
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor:.2f} de la cuenta. El nuevo saldo es ${self.saldo:.2f}")
            return True
        else:
            print("El valor a retirar debe ser mayor que cero y menor o igual que el saldo actual.")
            return False

def main():
    """
    Función principal para demostrar el uso de la clase CuentaBancaria.
    """
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, tipo.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)

if __name__ == "__main__":
    main()
