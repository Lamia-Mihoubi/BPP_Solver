
import math
from math import *
import numpy as np
import scipy
from scipy.stats import gamma


class simulation_chaotic:
    def __init__(
            self,
            max_iter,
            biotic_potential=3.9364481997283227


,


    ):
        self.max_iter = max_iter
        self.biotic_potential=biotic_potential
    def logistic_map(self,seed):
        values=[]
        for i in range(self.max_iter):
            next=self.biotic_potential*seed*(1-seed)
            values.append(next)
            seed=next

        return values

    #0.3< b<1.99
    def levy(self,n,beta=1.5):
        sigma = math.pow(
            gamma.rvs(1,1 + beta) * sin(beta * pi / 2) / (gamma.rvs(1,(1 + beta) / 2)) * beta * math.pow(2, (beta - 1) / 2),
            1 / beta)
        v = np.random.normal(0, sigma, n)
        u = np.random.normal(0, 1, n)
        z = u / np.power(np.abs(v), (1 / beta))
        return z

