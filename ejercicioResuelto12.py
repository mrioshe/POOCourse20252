class Calculos:
    """A class to perform salary-related calculations."""
    @staticmethod
    def calcular_salario_bruto(horas_laboradas, valor_hora):
        """Calculates the gross salary."""
        return horas_laboradas * valor_hora

    @staticmethod
    def calcular_porcentaje_retencion(retencion):
        """Converts the retention percentage to a decimal value."""
        return retencion / 100

    @staticmethod
    def calcular_retencion_fuente(porcentaje_retencion, salario_bruto):
        """Calculates the withholding tax amount."""
        return porcentaje_retencion * salario_bruto

    @staticmethod
    def calcular_salario_neto(salario_bruto, valor_retencion_fuente):
        """Calculates the net salary after deductions."""
        return salario_bruto - valor_retencion_fuente

def main():
    """Main function to get user input and display salary calculations."""
    try:
        horas_trabajadas = float(input("Ingresa las horas trabajadas: "))
        valor_hora = float(input("Ingresa el valor de la hora: "))
        retencion = float(input("Ingresa el porcentaje de retención en la fuente: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")
        return

    # Use the static methods from the Calculos class
    salario_bruto = Calculos.calcular_salario_bruto(horas_trabajadas, valor_hora)
    
    porcentaje_retencion = Calculos.calcular_porcentaje_retencion(retencion)
    
    valor_retencion_fuente = Calculos.calcular_retencion_fuente(porcentaje_retencion, salario_bruto)
    
    salario_neto = Calculos.calcular_salario_neto(salario_bruto, valor_retencion_fuente)
    
    print(f"\nSalario bruto: {salario_bruto}")
    print(f"Valor retención en la fuente: {valor_retencion_fuente}")
    print(f"Salario neto: {salario_neto}")

if __name__ == "__main__":
    main()