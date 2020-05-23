import random
from copy import deepcopy
import time

import numpy as np
import math

import Instances_reader
import Model
from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Méthodes_Heuristiques.BF_BFD import best_fit_dec
from Méthodes_Heuristiques.FF_FFD import first_fit_dec, first_fit
from Méthodes_Heuristiques.NF_NFD import nextfit


class RS:
    n = 0
    c = 0
    list = []

    def RS_iteratif(self, n, c, list, Tinit=30, T0=0.1, R=200, alpha=0.925):
        Sols = []
        vals = []
        deltaF, nb, sol = self.RS(n, c, list, Tinit, T0, R, alpha, init=True)
        Sols.append(sol)
        vals.append(nb)
        Tinit = min(100, abs(int(np.mean(deltaF) / math.log(0.8, 2))))
        print(Tinit)
        for i in range(10):
            # print(vals)
            nb, sol = self.RS(n, c, list, Tinit, T0, R, alpha)
            Sols.append(sol)
            vals.append(nb)
        print(vals)
        return min(vals), Sols[vals.index(min(vals))]

    def RS(self, n, c, list, Tinit, T0, R, alpha, init=False):
        deltaF = []
        self.n = n
        self.c = c
        self.list = list
        R = min(1000, int(n))
        # alpha = (1-1/n)
        # T0=Tinit/math.log(n,2)
        # Tinit= n
        """Solution initiale générée aléatoirement """
        random.shuffle(list)
        liste_obj = first_fit(list, c)
        Zs = len(liste_obj)
        S = []
        for i in range(Zs):
            S.append(Model.Bin(i, c))
            for j in range(len(liste_obj[i])):
                S[i].ranger_obj(Model.Objet(i + j, liste_obj[i][j]))

        """ initialisaiton des parametres"""
        Best = deepcopy(S)
        # Tinit=self.Temperature_initiale()
        T = Tinit
        # T0 = self.Temperature_min()
        Tmoy = (Tinit + T0) / 2  # la barriere entre le regime haute temperature et basse temperature

        """tant que le seuil de temperature n'est pas atteint, recherche locale avec la temperature T"""
        while T > T0:
            improve = False
            cpt = 0
            proba = -1
            # print(T)
            """repeter le processus de recherche locale R fois """
            for i in range(R):
                """generer aléatoirement une solution voisine de S"""
                v = random.uniform(0, 1)
                if T > Tmoy:
                    """Mode High temperature => Type1"""
                    Sprim = self.generer_voisin1(S)
                else:
                    """Mode Low temperature => Type2"""
                    Sprim = self.generer_voisin2(S)
                if init:
                    deltaF.append(self.F(S) - self.F(Sprim))

                if self.F(Sprim) > self.F(S):
                    """accepter Sprim """
                    S = deepcopy(Sprim)
                    if len(Sprim) < len(Best):
                        Best = deepcopy(Sprim)
                        improve = True
                        cpt = cpt + 1

                else:
                    """accepter Sprim avec un proba """
                    u = np.random.uniform(0, 1)
                    # print(((self.F(Sprim)-self.F(S))/T))
                    # print(math.exp((self.F(Sprim) - self.F(S)) / T))
                    proba = math.exp(-(self.F(S) - self.F(Sprim)) / T)
                    if u > proba:
                        S = deepcopy(Sprim)
                        if len(Sprim) < len(Best):
                            Best = deepcopy(Sprim)
                if cpt >= int(R / 2):
                    break
            if not improve and proba < 0.01:
                break
            """diminution de la temperature"""
            T = T * alpha

        if init:
            return deltaF, len(Best), Best
        else:
            return len(Best), Best

    def generer_voisin1(self, SS):  # regime haute temperature
        S = deepcopy(SS)
        random.shuffle(S)
        """idée: prendre un article aléatoire et le ranger dans une autre boite existante"""

        for b1 in range(len(S)):
            for o in range(len(S[b1].get_objects)):
                objet = S[b1].get_objects[o]
                # parcourir l'ensemble des boites et ranger l'objet dans la 1ere boite qui peut le contenir (FF)
                for b in range(len(S)):
                    if b != b1 and S[b].capacite_restante() >= objet.weight:
                        S[b].ranger_obj(objet)
                        S[b1].supprimer_obj(objet)
                        bsupp = S[b1]
                        if len(S[b1].get_objects) == 0:
                            S.remove(bsupp)
                        return S

        return S

    def generer_voisin2(self, SS):  # regime low temperature
        S = deepcopy(SS)
        """idée : prendre 2 objets aléatoirement, qui sont dans 2 boites differentes , et les permuter """
        random.shuffle(S)
        for b1_index in range(len(S)):  # indice premiere boite
            for o1_index in range(len(S[b1_index].get_objects)):  # indice objet 1
                objet1 = S[b1_index].get_objects[o1_index]

                for b2_index in range(len(S)):
                    if b2_index != b1_index:  # indice boite 2
                        objets = S[b2_index].get_objects
                        for o2_index in range(len(objets)):  # indice objet2
                            objet2 = S[b2_index].get_objects[o2_index]
                            # essayer la permutation
                            if objet1.weight > objet2.weight and S[b2_index].capacite_restante() >= (
                                    objet1.weight - objet2.weight):
                                copy_objet1 = deepcopy(objet1)
                                S[b1_index].ranger_obj2(objet2, o1_index)
                                S[b2_index].ranger_obj2(copy_objet1, o2_index)
                                return S

                            if objet1.weight < objet2.weight and S[b1_index].capacite_restante() >= (
                                    objet2.weight - objet1.weight):
                                copy_objet1 = deepcopy(objet1)
                                S[b1_index].ranger_obj2(objet2, o1_index)
                                S[b2_index].ranger_obj2(copy_objet1, o2_index)
                                return S

                            if objet1.weight == objet2.weight:
                                copy_objet1 = deepcopy(objet1)
                                S[b1_index].ranger_obj2(objet2, o1_index)
                                S[b2_index].ranger_obj2(copy_objet1, o2_index)
                                return S

        return S

    def Temperature_initiale(self):
        Tinit = (max(self.list) * (sum(self.list) - max(self.list))) / (math.log(self.n, 2))
        return Tinit

    def Temperature_min(self):
        Tzero = 2 * (min(self.list) ** 2) / math.log(self.n, 2)
        return Tzero

    def F(self, S):
        """fonction du cout qui calcule le taux de remplissage des boites"""
        f = 0
        for b in range(len(S)):
            sum = 0
            for o in range(len(S[b].get_objects)):
                sum = sum + S[b].get_objects[o].weight
            sum = sum ** 2
            f = f + sum
        return f


"""
n, c, list = Instances_reader.ReadInstance(
    "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe3" + "\\" + "HARD3.txt")
#n = 10
#c = 100
#list = [49, 41, 34, 33, 29, 26, 26, 22, 20, 19]
classrs = RS()
t_exec = time.time()
rs, SS = classrs.RS_iteratif(n, c, list)
t_exec = time.time() - t_exec

for b in range(len(SS)):
    print("boite")
    for o in range(len(SS[b].get_objects)):
        print(SS[b].get_objects[o])
opt = get_opt_sol(3, "HARD3.txt")
print(t_exec)
liste_obj = first_fit_dec(list, c)

# print("HARD8")
print("OPT {}".format(opt))
print("RS {}".format(rs))
print("FFD {}".format(len(liste_obj)))
print(liste_obj)
"""
