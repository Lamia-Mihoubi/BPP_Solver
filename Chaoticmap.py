import math
from math import *
import numpy as np
'''import scipy
from scipy.stats import gamma'''
import sys
sys.path.insert(1,"C:\\Users\\TRETEC\\Anaconda3\\Lib\\site-packages\\scipy")
sys.path.append("C:\\Users\\TRETEC\\Anaconda3\\Lib\\site-packages\\scipy\\stats")
sys.path.append("C:\\Users\\TRETEC\\Anaconda3\\Scripts")




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
    def levy(self,distance,solutionn,n,beta=1.5):
        a = np.random.gamma(shape=1+beta, scale=1, size=1)
        c=np.random.gamma(shape=1+beta, scale=1, size=1) * sin(beta * pi / 2) / (np.random.gamma(shape=(1+beta) / 2, scale=1, size=1) * beta * math.pow(2, (beta - 1) / 2))
        sigma = math.pow(c,1 / beta)
        v = np.random.normal(0, sigma, n)
        u = np.random.normal(0, 1, n)
        z = u*0.01*distance / np.power(np.abs(v), (1 / beta))
        solutionn=np.array(solutionn+z*np.random.rand(n))

        return solutionn

