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

    def RS(self, n, c, list, Tinit=20, T0=0.1, R=200, alpha=0.9):
        self.n = n
        self.c = c
        self.list = list
        """Solution initiale générée aleatoirement """

        """First fit applied to the random list"""
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
        T = Tinit
        # T0 = self.Temperature_min()
        Tmoy = (Tinit + T0) / 2  # la barriere entre le regime haute temperature et basse temperature

        """tant que le seuil de temperature n'est pas atteint, recherche locale avec la temperature T"""
        while T > T0:
            cpt = 0
            """repeter le processus de recherche locale R fois """
            for i in range(R):
                if cpt == 30:
                    break
                """generer aléatoirement une solution voisine de S"""
                if T >= Tmoy:
                    """Mode High temperature => Type1"""
                    Sprim = self.generer_voisin1(S)
                else:
                    """Mode Low temperature => Type2"""
                    Sprim = self.generer_voisin2(S)
                    # print("type2")
                if self.F(Sprim) > self.F(S):
                    """accepter Sprim """
                    S = deepcopy(Sprim)
                    cpt=0
                    if len(Sprim) < len(Best):
                        Best = deepcopy(Sprim)
                    # print("amelio 2 ")
                else:
                    cpt = cpt + 1
                    """accepter Sprim avec un proba """
                    u = np.random.uniform(0, 1)
                    proba = math.exp((len(S) - len(Sprim)) / T)
                    if u > proba:
                        S = deepcopy(Sprim)
                        if len(Sprim) < len(Best):
                            Best = deepcopy(Sprim)
                        # print("amelio2")
            """diminution de la temperature"""
            T = T * alpha

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

        for b1_index in range(len(SS)):  # indice premiere boite
            for o1_index in range(len(SS[b1_index].get_objects)):  # indice objet 1
                objet1 = S[b1_index].get_objects[o1_index]

                for b2_index in range(len(SS)):
                    if b2_index != b1_index:  # indice boite 2
                        for o2_index in range(len(SS[b2_index].get_objects)):  # indice objet2
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
        return 1000

    def Temperature_min(self):
        return 0.1

    def F(self, S):
        f = 0
        for b in range(len(S)):
            sum = 0
            for o in range(len(S[b].get_objects)):
                sum = sum + S[b].get_objects[o].weight
            sum = (sum / self.c) ** 2
            f = f + sum
        return f / len(S)


"""# n, c, list = Instances_reader.ReadInstance(
#   "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe3" + "\\" + "HARD1.txt")
t_exec = time.time()
n=10
c=100
list=[49,41,34,33,29,26,26,22,20,19]
classrs=RS()
rs, SS = classrs.RS(n, c, list)
for b in range (len(SS)):
    print("boite")
    for o in range (len( SS[b].get_objects)):
        print(SS[b].get_objects[o])
t_exec = time.time() - t_exec
#opt = get_opt_sol(3, "HARD1.txt")

liste_obj = first_fit_dec(list, c)
#print("HARD8")
#print("OPT {}".format(opt))
print("RS {}".format(rs))
print("FFD {}".format(len(liste_obj)))
print (liste_obj)

"""
