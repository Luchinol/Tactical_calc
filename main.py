import tkinter as tk
from calculadora.gui import CalculatorGUI

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana raíz
    app = CalculatorGUI(root)  # Pasa 'root' como padre
    app.mainloop()

if __name__ == "__main__":
    main()