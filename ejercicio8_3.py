import math
import tkinter as tk
from tkinter import messagebox

# =============================================================================
# CLASES DE FIGURAS GEOMÉTRICAS
# =============================================================================

class FiguraGeometrica:
    """Clase base para figuras geométricas."""
    def __init__(self):
        # En Python, los atributos privados se marcan con un guion bajo (aunque aún son accesibles)
        self._volumen = 0.0
        self._superficie = 0.0

    @property
    def volumen(self):
        """Getter para el volumen."""
        return self._volumen

    @volumen.setter
    def volumen(self, volumen):
        """Setter para el volumen."""
        self._volumen = volumen

    @property
    def superficie(self):
        """Getter para la superficie."""
        return self._superficie

    @superficie.setter
    def superficie(self, superficie):
        """Setter para la superficie."""
        self._superficie = superficie

    # Los métodos calcularVolumen() y calcularSuperficie() serán implementados
    # por las clases hijas.

# ---

class Cilindro(FiguraGeometrica):
    """Clase para representar y calcular un cilindro."""
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        # Llama a los métodos de cálculo y asigna los resultados a la clase base
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        """Calcula el volumen del cilindro."""
        # Math.PI en Java es math.pi en Python
        # Math.pow(x, y) en Java es x**y o pow(x, y) en Python
        volumen = math.pi * self.altura * (self.radio ** 2)
        return volumen

    def calcular_superficie(self):
        """Calcula la superficie del cilindro."""
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * (self.radio ** 2) # Área de las dos bases
        return area_lado_a + area_lado_b

# ---

class Esfera(FiguraGeometrica):
    """Clase para representar y calcular una esfera."""
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        """Calcula el volumen de la esfera."""
        # Se usa la fracción 4/3 o (4.0/3.0) para mayor precisión.
        volumen = (4.0/3.0) * math.pi * (self.radio ** 3)
        return volumen

    def calcular_superficie(self):
        """Calcula la superficie de la esfera."""
        superficie = 4.0 * math.pi * (self.radio ** 2)
        return superficie

# ---

class Piramide(FiguraGeometrica):
    """Clase para representar y calcular una pirámide con base cuadrada."""
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        """Calcula el volumen de la pirámide."""
        # Fórmula: (base^2 * altura) / 3
        volumen = ((self.base ** 2) * self.altura) / 3.0
        return volumen

    def calcular_superficie(self):
        """Calcula la superficie de la pirámide."""
        area_base = self.base ** 2
        # Fórmula para el área lateral (en una pirámide de base cuadrada): 2 * base * apotema
        area_lado = 2 * self.base * self.apotema
        return area_base + area_lado

# =============================================================================
# CLASES DE VENTANAS (GUI con Tkinter)
# =============================================================================

class VentanaCilindro(tk.Toplevel):
    """Ventana para calcular el cilindro."""
    def __init__(self, master):
        # Toplevel es análogo a un nuevo JFrame en Java
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)
        # El código Java usa un layout 'null', en Tkinter usaremos .place() para un efecto similar
        self.inicio()

    def inicio(self):
        """Inicializa los componentes de la interfaz."""
        # Componentes análogos a Swing (JLabel, JTextField, JButton)
        
        # Radio
        tk.Label(self, text="Radio (cms):").place(x=20, y=20, width=135, height=23)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=100, y=20, width=135, height=23)

        # Altura
        tk.Label(self, text="Altura (cms):").place(x=20, y=50, width=135, height=23)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=100, y=50, width=135, height=23)

        # Botón Calcular
        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_cilindro)
        self.calcular.place(x=100, y=80, width=135, height=23)

        # Resultados
        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=110, width=135, height=23)
        
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=140, width=135, height=23)

    def calcular_cilindro(self):
        """Maneja el evento de cálculo (actionPerformed en Java)."""
        try:
            # Obtiene y valida la entrada como float
            radio = float(self.campoRadio.get())
            altura = float(self.campoAltura.get())
            
            # Crea el objeto y calcula
            cilindro = Cilindro(radio, altura)
            
            # Actualiza las etiquetas de resultado, usando f-string para formato (similar a String.format)
            self.volumen_label.config(text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")
            
        except ValueError:
            # Manejo de error (similar a JOptionPane en Java)
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")


# ---

class VentanaEsfera(tk.Toplevel):
    """Ventana para calcular la esfera."""
    def __init__(self, master):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x210")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        """Inicializa los componentes de la interfaz."""
        
        # Radio
        tk.Label(self, text="Radio (cms):").place(x=20, y=20, width=135, height=23)
        self.campoRadio = tk.Entry(self)
        self.campoRadio.place(x=100, y=20, width=135, height=23)

        # Botón Calcular
        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_esfera)
        self.calcular.place(x=100, y=80, width=135, height=23)

        # Resultados
        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=110, width=135, height=23)
        
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=140, width=135, height=23)

    def calcular_esfera(self):
        """Maneja el evento de cálculo."""
        try:
            radio = float(self.campoRadio.get())
            
            esfera = Esfera(radio)
            
            self.volumen_label.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")


# ---

class VentanaPiramide(tk.Toplevel):
    """Ventana para calcular la pirámide."""
    def __init__(self, master):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("300x250") # Se ajusta un poco el tamaño para más campos
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        """Inicializa los componentes de la interfaz."""
        
        # Base
        tk.Label(self, text="Base (cms):").place(x=20, y=20, width=135, height=23)
        self.campoBase = tk.Entry(self)
        self.campoBase.place(x=120, y=20, width=135, height=23)

        # Altura
        tk.Label(self, text="Altura (cms):").place(x=20, y=50, width=135, height=23)
        self.campoAltura = tk.Entry(self)
        self.campoAltura.place(x=120, y=50, width=135, height=23)
        
        # Apotema
        tk.Label(self, text="Apotema (cms):").place(x=20, y=80, width=135, height=23)
        self.campoApotema = tk.Entry(self)
        self.campoApotema.place(x=120, y=80, width=135, height=23)

        # Botón Calcular
        self.calcular = tk.Button(self, text="Calcular", command=self.calcular_piramide)
        self.calcular.place(x=120, y=110, width=135, height=23)

        # Resultados
        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.place(x=20, y=140, width=135, height=23)
        
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.place(x=20, y=170, width=135, height=23)

    def calcular_piramide(self):
        """Maneja el evento de cálculo."""
        try:
            base = float(self.campoBase.get())
            altura = float(self.campoAltura.get())
            apotema = float(self.campoApotema.get())
            
            piramide = Piramide(base, altura, apotema)
            
            self.volumen_label.config(text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")

# ---

class VentanaPrincipal(tk.Tk):
    """Ventana principal que actúa como menú."""
    def __init__(self):
        super().__init__()
        self.title("Cálculo de Figuras Geométricas")
        self.geometry("300x150")
        self.resizable(False, False)
        self.inicio()
        
    def inicio(self):
        """Configura el menú principal."""
        
        tk.Label(self, text="Seleccione la figura a calcular:").pack(pady=10)
        
        # Frame para botones, usando FlowLayout implícito con .pack()
        button_frame = tk.Frame(self)
        button_frame.pack()
        
        tk.Button(button_frame, text="Cilindro", command=self.abrir_cilindro).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Esfera", command=self.abrir_esfera).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(button_frame, text="Pirámide", command=self.abrir_piramide).pack(side=tk.LEFT, padx=5, pady=5)
        
    def abrir_cilindro(self):
        """Abre la ventana del cilindro."""
        VentanaCilindro(self)

    def abrir_esfera(self):
        """Abre la ventana de la esfera."""
        VentanaEsfera(self)
        
    def abrir_piramide(self):
        """Abre la ventana de la pirámide."""
        VentanaPiramide(self)

# =============================================================================
# EJECUCIÓN DEL PROGRAMA (Main en Java)
# =============================================================================

if __name__ == "__main__":
    # La clase tk.Tk actúa como el contenedor principal de la aplicación,
    # similar a cómo se inicia el JFrame principal en Java.
    
    # Crea la ventana principal
    aplicacion = VentanaPrincipal() 
    
    # Inicia el bucle de eventos de Tkinter
    aplicacion.mainloop()