# calculadora/controllers/ahp_controller.py
from calculadora.models.ahp_model import AHPModel

class AHPController:
    def __init__(self, criteria):
        self.model = AHPModel(criteria)

    def compute_ahp(self, entries):
        """
        Recibe la matriz con valores (el triángulo superior) y delega en el modelo la
        construcción de la matriz completa y el cálculo de los pesos.
        """
        matrix = self.model.build_matrix(entries)
        weights = self.model.calculate_weights(matrix)
        return weights