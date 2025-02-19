# calculadora/ahp.py (fragmento modificado)
import tkinter as tk
from tkinter import ttk, messagebox
from calculadora.controllers.ahp_controller import AHPController

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
        self.matrix_widgets = []  # Almacena los widgets de la matriz (Entry o Label)
        self.create_widgets()

    def create_widgets(self):
        header = ttk.Label(self, text="Matriz de Comparación por Pares", font=("Arial", 14, "bold"))
        header.grid(row=0, column=0, columnspan=self.n+1, pady=10)

        # Encabezados de columna con los nombres de los criterios
        for j, crit in enumerate(self.criteria):
            lbl = ttk.Label(self, text=crit, borderwidth=1, relief="solid", padding=5)
            lbl.grid(row=1, column=j+1, sticky="nsew", padx=1, pady=1)

        # Filas: primer columna con el nombre y celdas de la matriz
        for i, crit in enumerate(self.criteria):
            lbl = ttk.Label(self, text=crit, borderwidth=1, relief="solid", padding=5)
            lbl.grid(row=i+2, column=0, sticky="nsew", padx=1, pady=1)
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
                    entry.insert(0, "1")
                    entry.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(entry)
                else:
                    lbl_val = ttk.Label(self, text="1.00", borderwidth=1, relief="solid", padding=5, anchor="center")
                    lbl_val.grid(row=i+2, column=j+1, padx=1, pady=1)
                    row_widgets.append(lbl_val)
            self.matrix_widgets.append(row_widgets)

        btn_calc = ttk.Button(self, text="Calcular AHP", command=self.calcular_ahp)
        btn_calc.grid(row=self.n+3, column=0, columnspan=self.n+1, pady=10)

        self.label_result = ttk.Label(self, text="Pesos: ", font=("Arial", 12))
        self.label_result.grid(row=self.n+4, column=0, columnspan=self.n+1, pady=10)

    def calcular_ahp(self):
        # Se crea una matriz de entrada solo con el triángulo superior editable
        entries = [[1.0 for _ in range(self.n)] for _ in range(self.n)]
        try:
            for i in range(self.n):
                for j in range(self.n):
                    if i == j:
                        entries[i][j] = 1.0
                    elif i < j:
                        widget = self.matrix_widgets[i][j]
                        val = float(widget.get())
                        if val <= 0:
                            messagebox.showerror("Error", "Los valores deben ser mayores que cero.")
                            return
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
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos en la matriz.")

# Permite probar la ventana AHP de forma independiente.
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ahp_window = AHPGUI(root)
    root.mainloop()