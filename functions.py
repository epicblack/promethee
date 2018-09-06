import numpy as np


class PreferenceFunctions:

    def usual_function(self, x):
        return 0 if x <= 0 else 1

    def quasi_criterion(self, x, q):
        return 0 if x <= q else 1

    def linear_function(self, x, p):
        return x/p if x <= p else 1

    def level_criterion(self, x, p, q):
        if x <= q:
            return 0
        if q < x <= q+p:
            return 0.5
        return 1

    def linear_with_indifference(self, x, p, q):
        if x <= q:
            return 0
        if q <= x <= p+q:
            return (x-q)/p
        return 1

    def gaussian_criteria(self, x, s):
        return 0 if x <= 0 else 1-np.exp(-x**2/(2*s**2))

    def get_preference_functions(self):
        return {
            'usual': self.usual_function,
            'linear': self.linear_function,
            'gaussian': self.gaussian_criteria,
            'quasi-criterion': self.quasi_criterion,
            'level': self.level_criterion,
            'linear_with_indifference': self.linear_with_indifference
        }
