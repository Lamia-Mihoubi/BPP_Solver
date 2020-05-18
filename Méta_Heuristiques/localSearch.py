import math
import os
import time

from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Méthodes_Heuristiques.BF_BFD import best_fit_dec
from copy import copy, deepcopy
import Instances_reader
import Model

class localsearch:
    dm = [[]]
    chd = []
    iter = 0

    def ameliorer_Sol(self, n, c, liste_obj):
        # appliquer BFD pour generer la solution initiale
        Zs, liste_obj = best_fit_dec(liste_obj, n, c)
        S = []
        for i in range(Zs):
            S.append(Model.Bin(i, c))

        for o in liste_obj:
            S[o[1]].ranger_obj(Model.Objet(liste_obj.index(o), o[0]))

        # ordonner les boites selon Ws croissant
        S.sort(key=lambda x: x.total_weight, reverse=True)
        # attribuer id des boites selon leur position
        for i in range(Zs):
            S[i].set_id(i)

        # initialisaiton des variables de controle
        self.iter = 0
        for i in range(Zs):
            self.chd.append(0)
            self.dm.append([])
            for j in range(Zs):
                self.dm[i].append(-1)
        improvement = True

        while improvement:
            # tant qu'on a trouvé une meilleure solution, on boucle encore
            improvement = False
            for j in range(len(S)):  # pour chaque boite j
                if not improvement:  # tant qu'on a pas trouver une sol realisable
                    self.iter = self.iter + 1
                    # obtenir une nouvelle solution S' (etapes 1-2-3)
                    # (1) eliminer la boite j de S
                    # (2) redistribuer ses articles sur les autres boites
                    Sprim = self.redistribute(S, j)
                    # (3) mettre a jour la date de modif des boites concernées
                    for i in range(len(S)):
                        for j in range(len(
                                Sprim)):  # """" les deux boucles pour parcourir les boites dans s et sprim et voir celle qui a changé"""
                            if S[i].id == Sprim[j].id and (S[i].total_weight != Sprim[j].total_weight):
                                self.chd[S[i].id] = self.iter

                    if self.realisable(Sprim):
                        # ie : apres redistribution on a obtenue une meilleure solution
                        S = deepcopy(Sprim)
                        Zs = len(S)
                        improvement = True

                    else:
                        Snv = self.recherche_locale(Sprim)
                        if self.realisable(Snv):
                            print("RL realisable")
                            S = deepcopy(Snv)
                            Zs = len(S)
                            improvement = True


        return S

    def realisable(self, S):
        if len(S) == 0:
            return False
        for bin in S:
            if bin.total_weight > bin.capacity:
                return False
        return True

    def redistribute(self, S, j):
        Sprim = deepcopy(S)
        if len(S) > 1:
            Bj = Sprim[j]  # la boite a eliminer et redistribuer
            for o in range(len(Bj.get_objects)):
                objet = Bj.get_objects[o]
                done = False
                for i in range(len(Sprim)):
                    if (i != j) and Sprim[i].capacite_restante() >= objet.weight:
                        Sprim[i].ranger_obj(objet)
                        done = True
                        break
                if not done:
                    Sprim[len(Sprim) - 1].ranger_obj(objet)
            del (Sprim[j])
        return []

    def recherche_locale(self, Sprim):
        local_improvement = True
        while not self.realisable(Sprim) and local_improvement:
            local_improvement = False
            for j in range(len(Sprim) - 1, 0, -1):
                while (not local_improvement) and Sprim[j].total_weight <= Sprim[j].capacity:
                    for i in range(j):
                        while not local_improvement:
                            # parcourir les boites deux a deux et pour chaque couple i  , j redistribuer
                            if self.couple_valide(Sprim, i, j):
                                self.dm[Sprim[i].id][Sprim[j].id] = self.iter
                                self.dm[Sprim[j].id][Sprim[i].id] = self.iter

                                # obtenir le voisin S'ij en utilisant KDM
                                items = Sprim[i].get_objects
                                items.append(Sprim[j].get_objects)
                                for k in range(len(items)):
                                    items[k] = items[k].weight
                                items.sort(reverse=True)
                                B1, B2 = self.KDM(items)
                                obj1 = []
                                obj2 = []
                                for b1 in range(len(B1)):
                                    obj1.append(Model.Objet(b1, B1[b1]))
                                for b2 in range(len(B2)):
                                    obj2.append(Model.Objet(b2, B2[b2]))
                                Sprimij = []
                                for k in range(len(Sprim)):
                                    Sprimij.append(Sprim[k])

                                Sprimij[i].set_obj(obj1)
                                Sprimij[j].set_obj(obj2)
                                # verifier si la solution obtenue reduit la violation de capacité
                                if abs(Sprimij[i].total_weight - Sprimij[j].total_weight) \
                                        < abs(Sprim[i].total_weight - Sprim[
                                    j].total_weight):  # on a reduit la violation de capacite
                                    Sprim = Sprimij
                                    local_improvement = True
                                    self.chd[Sprim[i].id] = self.iter
                                    self.chd[Sprim[j].id] = self.iter
        return Sprim

    def couple_valide(self, Sprim, i, j):
        valid = False
        i = Sprim[i].id
        j = Sprim[j].id
        max = max(self.chd[i], self.chd[j])
        if max > self.dm[i][j]:
            if Sprim[i].total_weight != Sprim[j].total_weight:
                valid = True
            else:
                self.dm[i][j] = self.iter
                self.dm[j][i] = self.iter
        return valid

    def KDM(self, items, B1=[], B2=[]):
        if len(items) == 1:
            print("trivial")
            B2.append(items[0])
        else:
            backup = []
            for i in range(len(items)):
                backup.append(items[i])
            val1 = items[0]
            val2 = items[1]
            diff = val1 - val2
            del (items[0])
            del (items[0])
            items.append(diff)
            items.sort(reverse=True)

            self.KDM(items, B1, B2)
            # search for couple with diff = difff
            B1.sort(reverse=True)
            B2.sort(reverse=True)
            done = False
            for i in range(len(B1)):
                if not done:
                    if (B1[i]) == diff:
                        del (B1[i])
                        done = True
            for i in range(len(B2)):
                if not done:
                    if (B2[i]) == diff:
                        done = True
                        del (B2[-1])
            B1.append(backup[1])
            B2.append(backup[0])
            B1.sort(reverse=True)
            B2.sort(reverse=True)

        return B1, B2


