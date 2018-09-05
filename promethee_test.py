import numpy as np
from functions import PreferenceFunctions
from promethee import Promethee

matrix = np.array([[80, 65, 83, 40, 52, 94],
                   [90, 58, 60, 80, 72, 96],
                   [60, 20, 40, 100, 60, 70],
                   [5.4, 9.7, 7.2, 7.5, 2, 3.6],
                   [8, 1, 4, 7, 3, 5],
                   [5, 1, 7, 10, 8, 6]])

pref = PreferenceFunctions(l=10, m=30, s=5, r=45, q=1, p=5, sigma=5)

criterions = np.array([
    pref.quasi_criterion,
    pref.linear_function,
    pref.linear_with_indifference,
    pref.level_criterion,
    pref.usual_function,
    pref.gaussian_criteria
])

minimize = [0, 2, 3, 4]

promethee = Promethee(matrix=matrix, minimize=minimize, criterions=criterions)

print(promethee.sort_alternatives())
