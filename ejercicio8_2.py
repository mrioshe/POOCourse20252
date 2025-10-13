import math
import tkinter as tk
from tkinter import messagebox
from typing import List

# =============================================================================
# CLASE DE CÁLCULO ESTADÍSTICO
# =============================================================================

class Notas:
    """Clase para almacenar y calcular el promedio, la desviación estándar,
    la nota mayor y la nota menor de una lista de 5 notas."""

    def __init__(self, lista_notas: List[float]):
        # El arreglo de Java (double[] listaNotas) se convierte en una lista de floats en Python
        # En el código Java, el array se inicializa a 5, por lo que asumimos que siempre
        # se pasará una lista con 5 notas.
        if len(lista_notas) != 5:
             raise ValueError("La lista de notas debe contener exactamente 5 elementos.")
        self.lista_notas = lista_notas

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las notas."""
        # En Python se usa la función sum() para simplificar la suma
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self) -> float:
        """Calcula la desviación estándar de las notas."""
        promedio = self.calcular_promedio()
        suma_cuadrados = 0
        
        # Iteración simplificada en Python (for-each style)
        for nota in self.lista_notas:
            # math.pow() en Python, o simplemente ** para elevar a una potencia
            suma_cuadrados += (nota - promedio) ** 2
            
        # math.sqrt() en Python
        return math.sqrt(suma_cuadrados / len(self.lista_notas))

    def calcular_menor(self) -> float:
        """Encuentra la nota mínima."""
        # Se usa la función min() de Python para simplificar el bucle de Java
        return min(self.lista_notas)

    def calcular_mayor(self) -> float:
        """Encuentra la nota máxima."""
        # Se usa la función max() de Python
        return max(self.lista_notas)

# =============================================================================
# CLASE DE INTERFAZ GRÁFICA (GUI con Tkinter)
# =============================================================================

class VentanaPrincipal(tk.Tk):
    """Ventana principal que permite ingresar 5 notas y calcular sus estadísticas."""

    def __init__(self):
        # tk.Tk() es el análogo al JFrame principal en Java
        super().__init__()
        self.title("Calculadora de Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.config(bg="#f0f0f0") # Simular color de fondo por defecto
        self.inicio()

    def inicio(self):
        """Inicializa los componentes de la interfaz (similar al layout null de Java)."""

        # Lista de campos de entrada para facilitar el acceso y la limpieza
        self.campos_nota: List[tk.Entry] = []
        
        # Coordenadas y etiquetas (JLabel y JTextField en Java -> tk.Label y tk.Entry en Python)
        
        for i in range(5):
            y_pos = 20 + i * 30
            
            # Etiqueta (Nota 1, Nota 2, etc.)
            tk.Label(self, text=f"Nota {i+1}:", bg="#f0f0f0").place(x=20, y=y_pos, width=70, height=23)
            
            # Campo de texto
            campo = tk.Entry(self, justify='center')
            campo.place(x=105, y=y_pos, width=135, height=23)
            self.campos_nota.append(campo)

        # Botones
        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_estadisticas)
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(self, text="Limpiar", command=self.limpiar_campos)
        self.limpiar.place(x=125, y=170, width=80, height=23)

        # Etiquetas de Resultados (inicializadas para que se puedan actualizar)
        self.promedio_label = tk.Label(self, text="Promedio =", anchor='w', bg="#f0f0f0")
        self.promedio_label.place(x=20, y=210, width=200, height=23)

        self.desviacion_label = tk.Label(self, text="Desviación =", anchor='w', bg="#f0f0f0")
        self.desviacion_label.place(x=20, y=240, width=200, height=23)

        self.mayor_label = tk.Label(self, text="Nota mayor =", anchor='w', bg="#f0f0f0")
        self.mayor_label.place(x=20, y=270, width=200, height=23)

        self.menor_label = tk.Label(self, text="Nota menor =", anchor='w', bg="#f0f0f0")
        self.menor_label.place(x=20, y=300, width=200, height=23)

    # El método actionPerformed de Java se divide en dos métodos separados:
    # calcular_estadisticas y limpiar_campos.

    def calcular_estadisticas(self):
        """Maneja el evento 'Calcular'."""
        try:
            # 1. Recoger y validar las notas
            notas_introducidas = []
            for campo in self.campos_nota:
                # Intenta convertir el texto a float
                nota = float(campo.get())
                notas_introducidas.append(nota)

            # 2. Crear objeto Notas y calcular
            calculo_notas = Notas(notas_introducidas)
            
            promedio = calculo_notas.calcular_promedio()
            desviacion = calculo_notas.calcular_desviacion()
            mayor = calculo_notas.calcular_mayor()
            menor = calculo_notas.calcular_menor()
            
            # 3. Mostrar resultados (usando .config para actualizar el texto)
            # El formato "%.2f" de Java se traduce al f-string de Python ":.2f"
            self.promedio_label.config(text=f"Promedio = {promedio:.2f}")
            self.desviacion_label.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.mayor_label.config(text=f"Nota mayor = {mayor}")
            self.menor_label.config(text=f"Nota menor = {menor}")

        except ValueError:
            # Captura errores si un campo está vacío o el formato no es numérico
            messagebox.showerror("Error de Entrada", "Asegúrate de ingresar un valor numérico en todas las 5 notas.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    def limpiar_campos(self):
        """Maneja el evento 'Limpiar'."""
        for campo in self.campos_nota:
            campo.delete(0, tk.END) # Borra todo el contenido del campo
            
        # Opcional: limpiar también los resultados
        self.promedio_label.config(text="Promedio = ")
        self.desviacion_label.config(text="Desviación = ")
        self.mayor_label.config(text="Nota mayor = ")
        self.menor_label.config(text="Nota menor = ")

# =============================================================================
# FUNCIÓN PRINCIPAL (Main en Java)
# =============================================================================

if __name__ == "__main__":
    # Este bloque ejecuta la aplicación cuando el archivo es llamado directamente
    app = VentanaPrincipal()
    app.mainloop()