# calculadora/models/ahp_model.py
import math

class AHPModel:
    def __init__(self, criteria):
        self.criteria = criteria
        self.n = len(criteria)

    def build_matrix(self, entries):
        """
        Construye la matriz completa a partir de la entrada.
        La entrada es una matriz (lista de listas) con los valores introducidos (solo el triángulo superior).
        """
        matrix = [[1.0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    matrix[i][j] = 1.0
                elif i < j:
                    matrix[i][j] = entries[i][j]
                else:
                    matrix[i][j] = 1.0 / entries[j][i]
        return matrix

    def calculate_weights(self, matrix):
        """
        Calcula los pesos utilizando la media geométrica de cada fila.
        """
        geom_means = []
        for i in range(self.n):
            prod = 1.0
            for j in range(self.n):
                prod *= matrix[i][j]
            gm = prod ** (1.0 / self.n)
            geom_means.append(gm)
        sum_gm = sum(geom_means)
        weights = [gm / sum_gm for gm in geom_means]
        return weights