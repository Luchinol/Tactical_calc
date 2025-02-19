# calculadora/ahp.py
import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
from calculadora.controllers.ahp_controller import AHPController

class ToolTip:
    def __init__(self, widget, text='Información'):
        self.waittime = 500     # en milisegundos
        self.wraplength = 180   # en píxeles
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def showtip(self, event=None):
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 10
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
            self.tw = None

class AHPGUI(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("AHP - Proceso de Análisis Jerárquico")
        self.minsize(700, 500)
        self.criteria = [
            "Movilidad",
            "Combate Nocturno",
            "Celeridad",
            "Flexibilidad",
            "Integracion Medios",
            "Integracion Apoyos"
        ]
        self.n = len(self.criteria)
        # Valores precargados para el triángulo superior (para i < j)
        # Lámina de comparación de valores sugeridos (puedes ajustar estos valores)
        self.default_matrix = [
            [None, 1.5, 1.2, 1.0, 0.8, 1.0],
            [None, None, 1.3, 1.1, 1.0, 1.2],
            [None, None, None, 1.0, 0.9, 1.1],
            [None, None, None, None, 1.2, 1.0],
            [None, None, None, None, None, 0.8],
            [None, None, None, None, None, None]
        ]
        self.matrix_widgets = []  # Almacena los widgets de la matriz (Entry o Label)
        self.dark_mode = False
        self._configure_styles()
        self.create_widgets()

    def _configure_styles(self):
        # Estilo para error en la validación de entradas
        style = ttk.Style(self)
        style.configure("Error.TEntry", fieldbackground="pink")
        # Configuración general (por defecto)
        style.configure("TEntry", fieldbackground="white")

    def create_widgets(self):
        header = ttk.Label(self, text="Matriz de Comparación por Pares (valores precargados)", font=("Arial", 14, "bold"))
        header.grid(row=0, column=0, columnspan=self.n+1, pady=10)
        ToolTip(header, "Matriz de comparaciones con valores sugeridos para cada criterio.")

        # Encabezados de columna con los nombres de los criterios
        for j, crit in enumerate(self.criteria):
            lbl = ttk.Label(self, text=crit, borderwidth=1, relief="solid", padding=5)
            lbl.grid(row=1, column=j+1, sticky="nsew", padx=1, pady=1)
            ToolTip(lbl, f"Columna para {crit}")

        # Filas: primer columna con el nombre de criterio y celdas de la matriz
        for i, crit in enumerate(self.criteria):
            lbl = ttk.Label(self, text=crit, borderwidth=1, relief="solid", padding=5)
            lbl.grid(row=i+2, column=0, sticky="nsew", padx=1, pady=1)
            ToolTip(lbl, f"Fila para {crit}")
            row_widgets = []
            for j in range(self.n):
                if i == j:
                    entry = ttk.Entry(self, width=7, justify="center")
                    entry.insert(0, "1")
                    entry.config(state="disabled")
                    entry.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(entry)
                elif i < j:
                    entry = ttk.Entry(self, width=7, justify="center")
                    # Pre-cargar el valor por defecto según la matriz precargada
                    default_val = self.default_matrix[i][j]
                    entry.insert(0, str(default_val) if default_val is not None else "1")
                    entry.grid(row=i+2, column=j+1, padx=1, pady=1)
                    ToolTip(entry, f"Ingrese el valor comparativo para {self.criteria[i]} vs {self.criteria[j]}")
                    row_widgets.append(entry)
                else:
                    lbl_val = ttk.Label(self, text="1.00", borderwidth=1, relief="solid", padding=5, anchor="center")
                    lbl_val.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(lbl_val)
            self.matrix_widgets.append(row_widgets)

        btn_calc = ttk.Button(self, text="Calcular AHP", command=self.calcular_ahp)
        btn_calc.grid(row=self.n+3, column=0, columnspan=self.n+1, pady=10)
        ToolTip(btn_calc, "Calcula los pesos utilizando el método AHP y muestra la gráfica de barras.")

        self.label_result = ttk.Label(self, text="Pesos: ", font=("Arial", 12))
        self.label_result.grid(row=self.n+4, column=0, columnspan=self.n+1, pady=10)

        # Botón para alternar entre tema claro y modo oscuro
        self.btn_toggle_theme = ttk.Button(self, text="Modo Oscuro: OFF", command=self.toggle_theme)
        self.btn_toggle_theme.grid(row=self.n+5, column=0, columnspan=self.n+1, pady=5)
        ToolTip(self.btn_toggle_theme, "Alterna entre modo oscuro y tema por defecto.")

    def calcular_ahp(self):
        # Restablecer el estilo de las entradas a por defecto antes de validar
        for i in range(self.n):
            for j in range(self.n):
                if i < j:
                    self.matrix_widgets[i][j].config(style="TEntry")

        entries = [[1.0 for _ in range(self.n)] for _ in range(self.n)]
        try:
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        entries[i][j] = 1.0
                    elif i < j:
                        widget = self.matrix_widgets[i][j]
                        try:
                            val = float(widget.get())
                        except ValueError:
                            widget.config(style="Error.TEntry")
                            raise ValueError("Valor no numérico")
                        if val <= 0:
                            widget.config(style="Error.TEntry")
                            raise ValueError("El valor debe ser mayor que cero")
                        entries[i][j] = val

            # Actualizar los labels en el triángulo inferior
            for i in range(self.n):
                for j in range(i):
                    self.matrix_widgets[i][j].config(text=f"{1.0 / entries[j][i]:.2f}")

            # Usar el controlador para el cálculo
            controller = AHPController(self.criteria)
            weights = controller.compute_ahp(entries)

            result_text = "Pesos:\n"
            for crit, weight in zip(self.criteria, weights):
                result_text += f"{crit}: {weight:.3f}\n"
            self.label_result.config(text=result_text)

            # Generar gráfica de barras
            plt.figure("AHP Weights")
            plt.clf()
            plt.bar(self.criteria, weights, color="#4a7abc")
            plt.xlabel("Criterios")
            plt.ylabel("Peso")
            plt.title("Distribución de Pesos AHP")
            plt.tight_layout()
            plt.show()

        except ValueError as ve:
            messagebox.showerror("Error", f"Por favor, ingresa valores numéricos válidos en la matriz.\nDetalle: {ve}")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        style = ttk.Style(self)
        if self.dark_mode:
            style.configure("TFrame", background="#2e2e2e")
            style.configure("TLabel", background="#2e2e2e", foreground="white")
            style.configure("TButton", background="#444", foreground="white")
            style.configure("TEntry", fieldbackground="#555", foreground="white")
            self.configure(background="#2e2e2e")
            self.btn_toggle_theme.config(text="Modo Oscuro: ON")
        else:
            style.configure("TFrame", background="SystemButtonFace")
            style.configure("TLabel", background="SystemButtonFace", foreground="black")
            style.configure("TButton", background="SystemButtonFace", foreground="black")
            style.configure("TEntry", fieldbackground="white", foreground="black")
            self.configure(background="SystemButtonFace")
            self.btn_toggle_theme.config(text="Modo Oscuro: OFF")

# Permite probar la ventana AHP de forma independiente.
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ahp_window = AHPGUI(root)
    root.mainloop()