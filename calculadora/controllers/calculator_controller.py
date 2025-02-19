# calculadora/controllers/calculator_controller.py

class CalculatorController:
    def calculate_total(self, unidades):
        """
        Recibe una lista de unidades (cada unidad es una lista de valores extraída de un Treeview)
        y calcula el puntaje total de la fuerza.
        """
        total = 0.0
        for unidad in unidades:
            try:
                # Se esperan los índices de: [Tipo, Cantidad, Movilidad, Combate Nocturno, Celeridad,
                # Flexibilidad, Integracion Medios, Integracion Apoyos]
                cantidad = float(unidad[1])
                movilidad = float(unidad[2])
                combate = float(unidad[3])
                celeridad = float(unidad[4])
                flexibilidad = float(unidad[5])
                integracion_medios = float(unidad[6])
                integracion_apoyos = float(unidad[7])
                puntaje = cantidad * (movilidad + combate + celeridad + flexibilidad + integracion_medios + integracion_apoyos)
                total += puntaje
            except (ValueError, IndexError):
                continue
        return total