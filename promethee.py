import numpy as np
from functions import PreferenceFunctions


class Promethee:

    def __init__(self, matrix, minimize):
        self.matrix = matrix
        self.minimize = minimize
        self.criterions = np.array([])

    def run(self):
        self.alternatives = self.compute_alternatives()
        self.ranking = self.sort_alternatives()

    def compute_alternatives(self):

        self.matrix[self.minimize, :] = self.matrix[self.minimize, :] * -1

        alternatives = self.matrix.shape[1]

        res = np.zeros((alternatives, alternatives))
        self.criterions = self.criterions.reshape((6, 2))
        for i in range(alternatives):
            for j in range(alternatives):
                v = self.matrix[:, i] > self.matrix[:, j]
                tmp = np.abs(self.matrix[v, i] - self.matrix[v, j])

                r = []

                for c, t in zip(self.criterions[v, :], tmp):
                    func = c[0]
                    param = c[1]
                    r.append(func(x=t, **param))
                res[i, j] = np.sum(r)/alternatives
        return res

    def add_function(self, function_name, **param):
        function = PreferenceFunctions().get_preference_functions()[
            function_name]
        self.criterions = np.append(
            self.criterions, np.array([function, param]), axis=0)

    def positive_flow(self):
        return self.alternatives.sum(axis=1)

    def negative_flow(self):
        return self.alternatives.sum(axis=0)

    def flow_diff(self):
        return self.positive_flow() - self.negative_flow()

    def sort_alternatives(self):
        best_alternatives = []
        for i, diff in enumerate(self.flow_diff()):
            best_alternatives.append((i+1, diff))
        return sorted(best_alternatives, key=lambda x: x[1], reverse=True)
