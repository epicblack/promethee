import numpy as np
from promethee import Promethee

matrix = np.array([[80, 65, 83, 40, 52, 94],
                   [90, 58, 60, 80, 72, 96],
                   [60, 20, 40, 100, 60, 70],
                   [5.4, 9.7, 7.2, 7.5, 2, 3.6],
                   [8, 1, 4, 7, 3, 5],
                   [5, 1, 7, 10, 8, 6]])

# matrix = np.array([[80, 65, 83, 40, 52, 94],
#                    [90, 58, 60, 80, 72, 96],
#                    [600, 200, 400, 1000, 600, 700],
#                    [54, 97, 72, 75, 20, 36],
#                    [8, 1, 4, 7, 3, 5],
#                    [5, 1, 7, 10, 8, 6]])

minimize = [0, 2, 3, 4]

promethee = Promethee(matrix=matrix, minimize=minimize)

promethee.add_function('quasi-criterion', q=10)
promethee.add_function('linear', p=30)
promethee.add_function('linear_with_indifference', q=5, p=45)
promethee.add_function('level', q=1, p=5)
promethee.add_function('usual')
promethee.add_function('gaussian', s=5)

promethee.run()

print(promethee.ranking)
