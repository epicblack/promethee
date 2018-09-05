import numpy as np
from functions import PreferenceFunctions


class Promethee:

    def __init__(self, matrix, minimize, criterions):
        self.matrix = matrix
        self.minimize = minimize
        self.criterions = criterions
        self.alternatives = self.compute_alternatives()

    def compute_alternatives(self):
        self.matrix[self.minimize, :] = self.matrix[self.minimize, :] * -1

        alternatives = self.matrix.shape[1]

        res = np.zeros((alternatives, alternatives))

        for i in range(alternatives):
            for j in range(alternatives):
                v = self.matrix[:, i] > self.matrix[:, j]
                tmp = np.abs(self.matrix[v, i] - self.matrix[v, j])

                r = []
                for c, t in zip(self.criterions[v], tmp):
                    r.append(c(t))
                res[i, j] = np.sum(r)/alternatives
        return res

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
