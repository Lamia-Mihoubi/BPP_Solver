
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