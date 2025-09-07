class Calculos:
    def calcular_edalber(self, ed_juan):
        """Calculates Alberto's age based on Juan's age."""
        ed_alber = 2 * (ed_juan / 3)
        return ed_alber

    def calcular_edana(self, ed_juan):
        """Calculates Ana's age based on Juan's age."""
        ed_ana = 4 * (ed_juan / 3)
        return ed_ana

    def calcular_edmama(self, ed_juan, ed_alber, ed_ana):
        """Calculates the mother's age as the sum of all children's ages."""
        ed_mama = ed_juan + ed_alber + ed_ana
        return ed_mama

class EjercicioResuelto4:
    def main(self):
        """Main method to execute the age calculations and print the results."""
        ed_juan = 9
        calculos = Calculos()
        
        ed_alber = calculos.calcular_edalber(ed_juan)
        ed_ana = calculos.calcular_edana(ed_juan)
        ed_mama = calculos.calcular_edmama(ed_juan, ed_alber, ed_ana)
        
        print("Las edades son:")
        print(f"Juan: {ed_juan}")
        print(f"Ana: {ed_ana}")
        print(f"Alberto: {ed_alber}")
        print(f"Mamá: {ed_mama}")

if __name__ == "__main__":
    ejercicio = EjercicioResuelto4()
    ejercicio.main()