# calculadora/ahp.py

import tkinter as tk
from tkinter import ttk, messagebox
import math

class AHPGUI(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("AHP - Proceso de Análisis Jerárquico")
        self.minsize(700, 500)
        self.criteria = [
            "Movilidad", "Combate Nocturno", "Celeridad",
            "Flexibilidad", "Integracion Medios", "Integracion Apoyos"
        ]
        self.n = len(self.criteria)
        self.matrix_widgets = []  # Almacenará referencias a los widgets (Entry o Label) para cada celda.
        self.create_widgets()

    def create_widgets(self):
        header = ttk.Label(self, text="Matriz de Comparación por Pares", font=("Arial", 14, "bold"))
        header.grid(row=0, column=0, columnspan=self.n+1, pady=10)

        # Encabezado de columnas con los nombres de los criterios.
        for j, crit in enumerate(self.criteria):
            lbl = ttk.Label(self, text=crit, borderwidth=1, relief="solid", padding=5)
            lbl.grid(row=1, column=j+1, sticky="nsew", padx=1, pady=1)

        # Filas: en la primera columna se muestra el nombre del criterio y luego se colocan las celdas de la matriz.
        for i, crit in enumerate(self.criteria):
            # Etiqueta para la fila
            lbl = ttk.Label(self, text=crit, borderwidth=1, relief="solid", padding=5)
            lbl.grid(row=i+2, column=0, sticky="nsew", padx=1, pady=1)
            row_widgets = []
            for j in range(self.n):
                if i == j:
                    # Diagonal: valor fijo de 1.
                    entry = ttk.Entry(self, width=7, justify="center")
                    entry.insert(0, "1")
                    entry.config(state="disabled")
                    entry.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(entry)
                elif i < j:
                    # Parte editable (triángulo superior): valor por defecto 1.
                    entry = ttk.Entry(self, width=7, justify="center")
                    entry.insert(0, "1")
                    entry.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(entry)
                else:
                    # Triángulo inferior: se muestra el recíproco, calculado automáticamente.
                    lbl_val = ttk.Label(self, text="1.00", borderwidth=1, relief="solid", padding=5, anchor="center")
                    lbl_val.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(lbl_val)
            self.matrix_widgets.append(row_widgets)

        # Botón para calcular los pesos AHP a partir de la matriz.
        btn_calc = ttk.Button(self, text="Calcular AHP", command=self.calcular_ahp)
        btn_calc.grid(row=self.n+3, column=0, columnspan=self.n+1, pady=10)

        # Etiqueta para mostrar los pesos calculados.
        self.label_result = ttk.Label(self, text="Pesos: ", font=("Arial", 12))
        self.label_result.grid(row=self.n+4, column=0, columnspan=self.n+1, pady=10)

    def calcular_ahp(self):
        """
        Esta función construye la matriz completa utilizando los valores ingresados
        en el triángulo superior y calcula los pesos mediante la media geométrica.
        Luego normaliza dichos valores y actualiza la interfaz.
        """
        matrix = [[1.0 for _ in range(self.n)] for _ in range(self.n)]
        try:
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        matrix[i][j] = 1.0
                    elif i < j:
                        widget = self.matrix_widgets[i][j]
                        val = float(widget.get())
                        if val <= 0:
                            messagebox.showerror("Error", "Los valores deben ser mayores que cero.")
                            return
                        matrix[i][j] = val
                    else:
                        # Para celdas inferiores: se calcula el recíproco del valor correspondiente en la parte superior.
                        matrix[i][j] = 1.0 / float(self.matrix_widgets[j][i].get())
                        # Actualiza el Label del triángulo inferior.
                        self.matrix_widgets[i][j].config(text=f"{matrix[i][j]:.2f}")

            # Cálculo de la media geométrica por fila.
            geom_means = []
            for i in range(self.n):
                prod = 1.0
                for j in range(self.n):
                    prod *= matrix[i][j]
                gm = prod ** (1.0/self.n)
                geom_means.append(gm)
            sum_gm = sum(geom_means)
            weights = [gm / sum_gm for gm in geom_means]

            # Construye el texto de resultado.
            result_text = "Pesos:\n"
            for crit, weight in zip(self.criteria, weights):
                result_text += f"{crit}: {weight:.3f}\n"
            self.label_result.config(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos en la matriz.")

# Permite probar la ventana AHP de forma independiente.
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    ahp_window = AHPGUI(root)
    root.mainloop()