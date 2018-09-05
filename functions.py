import numpy as np


class PreferenceFunctions:

    def __init__(self, p=None, q=None, r=None, s=None, l=None, m=None, sigma=None):
        self.p = p
        self.q = q
        self.r = r
        self.s = s
        self.l = l
        self.m = m
        self.sigma = sigma

    def usual_function(self, x):
        return 0 if x <= 0 else 1

    def quasi_criterion(self, x):
        return 0 if x <= self.l else 1

    def linear_function(self, x):
        return x/self.m if x <= self.m else 1

    def level_criterion(self, x):
        if x <= self.q:
            return 0
        if self.q < x <= self.q+self.p:
            return 0.5
        return 1

    def linear_with_indifference(self, x):
        if x <= self.s:
            return 0
        if self.s <= x <= self.s+self.r:
            return (x-self.s)/self.r
        return 1

    def gaussian_criteria(self, x):
        return 0 if x <= 0 else 1-np.exp(-x**2/(2*self.sigma**2))

    def get_preference_functions(self):
        return {
            'usual': self.usual_function,
            'linear': self.linear_function,
            'gaussian': self.gaussian_criteria,
            'quasi-criterion': self.quasi_criterion,
            'level': self.level_criterion,
            'linear_with_indifference': self.linear_with_indifference
        }
