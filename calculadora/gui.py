# calculadora/gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from calculadora.tropas import get_friendly_forces, get_adversary_structure
from calculadora.controllers.calculator_controller import CalculatorController

class ToolTip:
    def __init__(self, widget, text='Información'):
        self.waittime = 500
        self.wraplength = 180
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

# ----------------------------------------------------------------------
# Ventana de Lanzador (Launcher)
# ----------------------------------------------------------------------
class LauncherGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Selección de Fuerzas y Calculadora")
        self.minsize(1000, 600)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        frame_main = ttk.Frame(self)
        frame_main.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        frame_main.grid_rowconfigure(0, weight=1)
        frame_main.grid_columnconfigure(0, weight=1)
        frame_main.grid_columnconfigure(1, weight=1)

        # Panel para Fuerza Propia
        frame_friendly = ttk.LabelFrame(frame_main, text="Fuerza Propia")
        frame_friendly.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        frame_friendly.grid_rowconfigure(0, weight=1)
        frame_friendly.grid_columnconfigure(0, weight=1)

        columns_friendly = ("Unidad Superior", "Unidades Subordinadas", "UF", "Cantidad UF", "Tipo de Medios", "Cantidad Medios/U.F.")
        self.tree_friendly = ttk.Treeview(frame_friendly, columns=columns_friendly, show="headings")
        for col in columns_friendly:
            self.tree_friendly.heading(col, text=col)
            self.tree_friendly.column(col, width=150, anchor="center")
        self.tree_friendly.pack(expand=True, fill="both", padx=5, pady=5)
        for row in get_friendly_forces():
            self.tree_friendly.insert("", "end", values=row)
        ToolTip(self.tree_friendly, "Muestra las tropas de Fuerza Propia")

        # Panel para Fuerza Adversaria
        frame_adversary = ttk.LabelFrame(frame_main, text="Fuerza Adversaria")
        frame_adversary.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        frame_adversary.grid_rowconfigure(0, weight=1)
        frame_adversary.grid_columnconfigure(0, weight=1)

        self.tree_adversary = ttk.Treeview(frame_adversary)
        self.tree_adversary.heading("#0", text="Estructura de Unidades Adversarias", anchor="w")
        self.tree_adversary.pack(expand=True, fill="both", padx=5, pady=5)
        for grupo in get_adversary_structure():
            nodo = self.tree_adversary.insert("", "end", text=grupo["unidad_superior"], open=False)
            for sub in grupo["subordinados"]:
                hijo_text = sub.get("unidad_subordinada", "")
                self.tree_adversary.insert(nodo, "end", text=hijo_text, open=False)
        ToolTip(self.tree_adversary, "Muestra la estructura de la Fuerza Adversaria")

        btn_launch = ttk.Button(frame_main, text="Ingresar a la Calculadora", command=self.launch_calculator)
        btn_launch.grid(row=1, column=0, columnspan=2, pady=10)
        ToolTip(btn_launch, "Abre la ventana de la Calculadora")

        # Botón para toggle de tema oscuro en el Launcher
        self.btn_toggle_theme = ttk.Button(frame_main, text="Modo Oscuro: OFF", command=self.toggle_theme)
        self.btn_toggle_theme.grid(row=2, column=0, columnspan=2, pady=5)
        ToolTip(self.btn_toggle_theme, "Alterna entre modo oscuro y tema por defecto")

    def launch_calculator(self):
        self.withdraw()  # Oculta el Launcher
        CalculatorGUI(self)

    def toggle_theme(self):
        self.dark_mode = getattr(self, "dark_mode", False)
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

# ----------------------------------------------------------------------
# Ventana de la Calculadora
# ----------------------------------------------------------------------
class CalculatorGUI(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.title("Calculadora de Maniobras de Combate")
        self.minsize(800, 600)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.dark_mode = False

        # Configurar estilos (incluyendo el estilo para error en entradas)
        style = ttk.Style(self)
        style.configure("Error.TEntry", fieldbackground="pink")
        style.configure("TEntry", fieldbackground="white")

        # Botón para alternar tema oscuro
        self.btn_toggle_theme = ttk.Button(self, text="Modo Oscuro: OFF", command=self.toggle_theme)
        self.btn_toggle_theme.grid(row=4, column=0, columnspan=2, pady=5)
        ToolTip(self.btn_toggle_theme, "Alterna entre modo oscuro y tema por defecto")

        # Inicializar el controlador de la calculadora
        self.calc_controller = CalculatorController()

        # Panel para Fuerza Propia
        self.frame_own = ttk.LabelFrame(self, text="Fuerza Propia")
        self.frame_own.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_own.grid_rowconfigure(0, weight=1)
        self.frame_own.grid_columnconfigure(0, weight=1)
        self.notebook_own = ttk.Notebook(self.frame_own)
        self.notebook_own.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.tab_agregar_own = ttk.Frame(self.notebook_own)
        self.notebook_own.add(self.tab_agregar_own, text="Agregar Unidades")
        self.inputs_own = {}
        self.crear_panel_unidades(self.tab_agregar_own, self.inputs_own, is_own=True)

        # Panel para Fuerza Adversaria
        self.frame_adv = ttk.LabelFrame(self, text="Fuerza Adversaria")
        self.frame_adv.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frame_adv.grid_rowconfigure(0, weight=1)
        self.frame_adv.grid_columnconfigure(0, weight=1)
        self.notebook_adv = ttk.Notebook(self.frame_adv)
        self.notebook_adv.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.tab_agregar_adv = ttk.Frame(self.notebook_adv)
        self.notebook_adv.add(self.tab_agregar_adv, text="Agregar Unidades")
        self.inputs_adv = {}
        self.crear_panel_unidades(self.tab_agregar_adv, self.inputs_adv, is_own=False)

        # Panel de Resultados
        self.frame_resultados = ttk.Frame(self)
        self.frame_resultados.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
        self.frame_resultados.columnconfigure(0, weight=1)
        self.frame_resultados.columnconfigure(1, weight=1)
        self.label_total_own = ttk.Label(self.frame_resultados, text="Total Fuerza Propia: 0.00", font=("Arial", 12))
        self.label_total_own.grid(row=0, column=0, padx=20, pady=5, sticky="ew")
        self.label_total_adv = ttk.Label(self.frame_resultados, text="Total Fuerza Adversaria: 0.00", font=("Arial", 12))
        self.label_total_adv.grid(row=0, column=1, padx=20, pady=5, sticky="ew")
        self.label_advantage = ttk.Label(self.frame_resultados, text="Ventaja de Maniobra: 0.00", font=("Arial", 14, "bold"))
        self.label_advantage.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        # Botón para abrir la ventana de carga de tropas registradas
        self.btn_cargar_tropas = ttk.Button(self, text="Cargar Tropas Registradas", command=self.abrir_cargar_tropas)
        self.btn_cargar_tropas.grid(row=2, column=0, columnspan=2, pady=10)
        ToolTip(self.btn_cargar_tropas, "Carga las tropas predefinidas a la Calculadora")

        btn_ahp = ttk.Button(self, text="Evaluar AHP", command=self.abrir_ahp)
        btn_ahp.grid(row=3, column=0, columnspan=2, pady=10)
        ToolTip(btn_ahp, "Abre la ventana AHP para evaluar criterios")

    def abrir_ahp(self):
        from calculadora.ahp import AHPGUI
        self.ahp_win = AHPGUI(self)

    def on_close(self):
        self.destroy()
        if self.parent:
            self.parent.deiconify()

    def crear_panel_unidades(self, parent, inputs, is_own=True):
        container = ttk.Frame(parent)
        container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        panel_entrada = ttk.Frame(container)
        panel_entrada.grid(row=0, column=0, sticky="nw")

        # Definir las categorías OTAN y sus subcategorías
        categories_otan = {
            "Infantería": ["Infantería Mecanizada", "Infantería Blindada", "Infantería Motorizada"],
            "Caballería": ["Caballería Blindada", "Caballería Mecanizada"],
            "Artillería": ["Obuses Autopropulsados", "Artillería de Campaña"],
            "Ingeniería": ["Unidad de Ingenieros"],
            "Logística": ["Unidad Logística"]
        }
        options = [f"{cat} - {sub}" for cat, subs in categories_otan.items() for sub in subs]

        lbl_tipo = ttk.Label(panel_entrada, text="Tipo de Unidad:")
        lbl_tipo.grid(row=0, column=0, sticky="w", pady=2)
        tipo_combo = ttk.Combobox(panel_entrada, values=options, state="readonly", width=25)
        tipo_combo.grid(row=0, column=1, padx=5, pady=2)
        tipo_combo.current(0)
        inputs["Tipo"] = tipo_combo
        ToolTip(tipo_combo, "Seleccione el tipo de unidad")

        lbl_cantidad = ttk.Label(panel_entrada, text="Cantidad:")
        lbl_cantidad.grid(row=1, column=0, sticky="w", pady=2)
        cantidad_entry = ttk.Entry(panel_entrada, width=14)
        cantidad_entry.grid(row=1, column=1, padx=5, pady=2)
        inputs["Cantidad"] = cantidad_entry
        ToolTip(cantidad_entry, "Ingrese la cantidad de la unidad")

        subfactores = ["Movilidad", "Combate Nocturno", "Celeridad", "Flexibilidad",
                       "Integracion Medios", "Integracion Apoyos"]
        for idx, subf in enumerate(subfactores):
            lbl = ttk.Label(panel_entrada, text=f"{subf}:")
            lbl.grid(row=idx + 2, column=0, sticky="w", pady=2)
            entry = ttk.Entry(panel_entrada, width=14)
            entry.grid(row=idx + 2, column=1, padx=5, pady=2)
            inputs[subf] = entry
            ToolTip(entry, f"Ingrese el valor para {subf}")

        if is_own:
            btn = ttk.Button(panel_entrada, text="Agregar Unidad", command=self.agregar_unidad_own)
        else:
            btn = ttk.Button(panel_entrada, text="Agregar Unidad", command=self.agregar_unidad_adv)
        btn.grid(row=len(subfactores) + 2, column=0, columnspan=2, pady=5)
        ToolTip(btn, "Agrega la unidad a la lista")

        columnas = ("Tipo", "Cantidad", "Movilidad", "Combate Nocturno", "Celeridad",
                    "Flexibilidad", "Integracion Medios", "Integracion Apoyos")
        tree = ttk.Treeview(container, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor="center")
        tree.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        inputs["tree"] = tree

    def agregar_unidad_own(self):
        self.agregar_unidad(self.inputs_own)

    def agregar_unidad_adv(self):
        self.agregar_unidad(self.inputs_adv)

    def agregar_unidad(self, inputs):
        # Restablecer estilo de entradas a valor por defecto
        for key in inputs:
            if key != "tree":
                try:
                    inputs[key].config(style="TEntry")
                except:
                    pass
        try:
            tipo = inputs["Tipo"].get()
            cantidad = float(inputs["Cantidad"].get())
            movilidad = float(inputs["Movilidad"].get())
            combate = float(inputs["Combate Nocturno"].get())
            celeridad = float(inputs["Celeridad"].get())
            flexibilidad = float(inputs["Flexibilidad"].get())
            integracion_medios = float(inputs["Integracion Medios"].get())
            integracion_apoyos = float(inputs["Integracion Apoyos"].get())
            valores = [tipo, cantidad, movilidad, combate, celeridad, flexibilidad,
                       integracion_medios, integracion_apoyos]
            inputs["tree"].insert("", "end", values=valores)
            inputs["Cantidad"].delete(0, tk.END)
            inputs["Movilidad"].delete(0, tk.END)
            inputs["Combate Nocturno"].delete(0, tk.END)
            inputs["Celeridad"].delete(0, tk.END)
            inputs["Flexibilidad"].delete(0, tk.END)
            inputs["Integracion Medios"].delete(0, tk.END)
            inputs["Integracion Apoyos"].delete(0, tk.END)
            self.recalcular_totales()
        except ValueError:
            # Destaca los campos que puedan generar error
            for key in inputs:
                if key != "tree":
                    inputs[key].config(style="Error.TEntry")
            messagebox.showerror("Error de entrada", "Por favor, ingresa valores numéricos válidos.")

    def recalcular_totales(self):
        own_units = [self.inputs_own["tree"].item(child)["values"] for child in self.inputs_own["tree"].get_children()]
        adv_units = [self.inputs_adv["tree"].item(child)["values"] for child in self.inputs_adv["tree"].get_children()]
        total_own = self.calc_controller.calculate_total(own_units)
        total_adv = self.calc_controller.calculate_total(adv_units)
        self.label_total_own.config(text=f"Total Fuerza Propia: {total_own:.2f}")
        self.label_total_adv.config(text=f"Total Fuerza Adversaria: {total_adv:.2f}")
        self.label_advantage.config(text=f"Ventaja de Maniobra: {(total_own - total_adv):.2f}")

    def abrir_cargar_tropas(self):
        CargarTropasGUI(self)

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

# ----------------------------------------------------------------------
# Ventana para Cargar Tropas Registradas
# ----------------------------------------------------------------------
class CargarTropasGUI(tk.Toplevel):
    def __init__(self, calculator):
        super().__init__(calculator)
        self.calculator = calculator
        self.title("Cargar Tropas Registradas")
        self.minsize(600, 400)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.tab_friendly = ttk.Frame(notebook)
        notebook.add(self.tab_friendly, text="Fuerza Propia")
        self.crear_panel_friendly(self.tab_friendly)

        self.tab_adversary = ttk.Frame(notebook)
        notebook.add(self.tab_adversary, text="Fuerza Adversaria")
        self.crear_panel_adversary(self.tab_adversary)

    def crear_panel_friendly(self, parent):
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        self.tree_friendly = ttk.Treeview(parent,
            columns=("Unidad Superior", "Unidades Subordinadas", "UF", "Cantidad UF", "Tipo de Medios", "Cantidad Medios/U.F."),
            show="headings")
        for col in ("Unidad Superior", "Unidades Subordinadas", "UF", "Cantidad UF", "Tipo de Medios", "Cantidad Medios/U.F."):
            self.tree_friendly.heading(col, text=col)
            self.tree_friendly.column(col, width=100, anchor="center")
        self.tree_friendly.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        friendly_data = get_friendly_forces()
        for row in friendly_data:
            self.tree_friendly.insert("", "end", values=row)

        btn_cargar = ttk.Button(parent, text="Cargar a Calculadora", command=self.cargar_friendly)
        btn_cargar.grid(row=1, column=0, pady=5)

    def cargar_friendly(self):
        selected = self.tree_friendly.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione una tropa de Fuerza Propia para cargar.")
            return
        data = self.tree_friendly.item(selected[0])["values"]
        try:
            tipo = data[2]
            cantidad = float(data[3])
        except (IndexError, ValueError):
            messagebox.showerror("Error", "Datos inválidos en la tropa seleccionada.")
            return
        if len(data) >= 12:
            subfactores = list(data[6:12])
        else:
            subfactores = [1.0] * 6
        nuevos_valores = [tipo, cantidad] + subfactores
        self.calculator.inputs_own["tree"].insert("", "end", values=nuevos_valores)
        self.calculator.recalcular_totales()
        messagebox.showinfo("Carga Exitosa", "Tropa de Fuerza Propia cargada a la Calculadora.")

    def crear_panel_adversary(self, parent):
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        columns = ("Unidad Subordinada", "Pequeña Unidad", "Cantidad", "Tipo de Medios", "Cant Medios/UF")
        self.tree_adversary = ttk.Treeview(parent, columns=columns, show="tree headings")
        self.tree_adversary.heading("#0", text="Unidad Superior", anchor="w")
        self.tree_adversary.column("#0", width=200, anchor="w")
        for col in columns:
            self.tree_adversary.heading(col, text=col, anchor="center")
            self.tree_adversary.column(col, width=150, anchor="center")
        self.tree_adversary.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        for grupo in get_adversary_structure():
            nodo = self.tree_adversary.insert("", "end", text=grupo["unidad_superior"], open=True, values=("", "", "", "", ""))
            for sub in grupo["subordinados"]:
                values = (
                    sub.get("unidad_subordinada", ""),
                    sub.get("pequeña_unidad", ""),
                    sub.get("cantidad", ""),
                    sub.get("tipo_medios", ""),
                    sub.get("cantidad_medios_por_uf", "")
                )
                self.tree_adversary.insert(nodo, "end", text="", values=values)
        btn_cargar = ttk.Button(parent, text="Cargar a Calculadora", command=self.cargar_adversary)
        btn_cargar.grid(row=1, column=0, pady=5)

    def cargar_adversary(self):
        selected = self.tree_adversary.selection()
        if not selected:
            messagebox.showerror("Error", "Seleccione una unidad adversaria (nodo hoja) para cargar.")
            return
        if self.tree_adversary.get_children(selected[0]):
            messagebox.showerror("Error", "Seleccione un nodo hoja para cargar.")
            return
        item_data = self.tree_adversary.item(selected[0])
        if not item_data["text"]:
            if item_data["values"]:
                tipo = item_data["values"][0]
            else:
                messagebox.showerror("Error", "No se pudo determinar la unidad adversaria.")
                return
        else:
            tipo = item_data["text"]
        cantidad = 1.0
        from calculadora.tropas import get_adversary_structure
        ahp_values = [1.0] * 6
        estructura = get_adversary_structure()
        for grupo in estructura:
            for sub in grupo.get("subordinados", []):
                if sub.get("unidad_subordinada", "") == tipo:
                    if "ahp" in sub and sub["ahp"] is not None:
                        ahp_values = sub["ahp"]
                        break
        nuevos_valores = [tipo, cantidad] + ahp_values
        self.calculator.inputs_adv["tree"].insert("", "end", values=nuevos_valores)
        self.calculator.recalcular_totales()
        messagebox.showinfo("Carga Exitosa", "Tropa de Fuerza Adversaria cargada a la Calculadora.")

# ----------------------------------------------------------------------
# Inicio de la aplicación (para pruebas independientes)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = LauncherGUI()
    app.mainloop()