
from scipy.stats import gamma

class simulation_chaotic:
    def __init__(
            self,
            biotic_potential=3.9364481997283227,
            max_iter=50,

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
    '''''
    def levy(self,beta,n):
        sigma = math.pow(
            gamma(1 + beta) * sin(beta * 3.14 / 2) / (gamma((1 + beta) / 2)) * beta * math.pow(2, (beta - 1) / 2),
            1 / beta)
        v = np.random.normal(0, sigma, n)
        u = np.random.normal(0, 1, n)
        z = u / np.power(np.abs(v), (1 / beta))
        return z
    cho=simulation_chaotic()
    cho.levy(1.5,3)
    '''
