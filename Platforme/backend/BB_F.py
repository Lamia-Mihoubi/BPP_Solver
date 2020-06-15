# Dans ce fichier on implemente une version améliorée de l'algorithme Branch and Bound pour résoudre
# le problème Bin Packing à une dimension
# l'amelioration consiste a utiliser l'heuristique WFD pour initialiser la solution optimale
# et l'utilisation de la borne L2 pour l'élagage des neouds

import math
import sys
import numpy as np


class Binpacker(object):
    # DECLARATION DES VARIABLES GLOBALES
    n = 0
    c = 0
    listobj = []
    optcost = sys.maxsize
    optlist = []

    def init(self, n, c, list):
        self.n = n
        self.c = c
        self.listobj = list
        self.optcost = self.wfd()

    def permuter(self, a, b):  # permuter entre 2 objets de la liste
        x = 0
        x = self.listobj[a]
        self.listobj[a] = self.listobj[b]
        self.listobj[b] = x

    def wfd(self):
        self.optlist = []
        listobj = self.listobj
        for i in range(len(listobj)):
            self.optlist.append(listobj[i])
        # ordonne la liste optlist
        self.optlist.sort(reverse=True)
        bins2 = [0]
        lastbin = 0
        for wix in range(self.n):  # pour chaque poids d'un objet
            bins2.sort()  # ordonner les boites par ordre decroissant de capacité restante
            done = False
            wt = self.optlist[wix]  # poids de l'objet wix
            for bix in range(lastbin):  # parcourir les boites ouvertes
                if (wt + bins2[bix]) <= self.c:  # objet wt peut être ranger dans bix
                    bins2[bix] = bins2[bix] + wt  # ranger wt dans bix
                    done = True
                    break
            if not done:  # l'objet ne peut être ranger dans aucune boîte
                lastbin = lastbin + 1  # ouverture d'une nouvelle boîte
                bins2.append(0)
                bins2[lastbin] = wt  # ranger l'objet dans la nouvelle boîte
        return lastbin + 1

    def Bound_L2(self, k):
        listobj = self.listobj
        n = self.n
        c = self.c
        optcost = self.optcost
        optlist = self.optlist

        # recuperer les poids qui sont inferieurs a C/2
        V = np.unique(listobj)
        V = V[V < (c / 2)]
        L = []

        for j in V:
            # calculer J1 ,J2 et J3
            J1 = []
            J2 = []
            J3 = []
            for i in range(k, n - 1):
                if (c - j) < listobj[i]:
                    J1.append(listobj[i])
                else:
                    if (c / 2) < listobj[i]:
                        J2.append(listobj[i])
                if (j <= listobj[i]) and (listobj[i] <= (c / 2)):
                    J3.append(listobj[i])
            # calcul Lj

            L.append(len(J1) + len(J2) + max((sum(J3) - ((len(J2) * c) - sum(J2))) / c, 0))
        L2 = max(L)
        return L2

    def packBins_BBA(self, k, sumwts, bcount, capa_restante):
        # recherche en profondeur dans un arbre
        # k=ordre de l'objet à etre affecter ( profondeur du noeud)
        # sumwts = somme cumulée des poids des objets restants
        # bcount= somme cumulée du nombre de boîtes utiliséés jusqu'a ce noeud
        # cap_restante= espace libre restant dans la boîte ouverte
        optcost = self.optcost
        listobj = self.listobj
        n = self.n
        c = self.c

        if k == n:  # le noeud actuel est une feuille ( solution exacte)
            # verifier si la solution obtenue est meilleure que la solution optimale
            if bcount < optcost:

                # mettre à jour la solution optimale
                optcost = bcount
                self.optlist = []
                # sauvegarder la solution dans opt_list
                for i in range(n):
                    self.optlist.append(listobj[i])
        else:  # le noeud actuel est un noeud de décision
            for i in range(k, n):  # pour tout objet restant, essayer ce dernier
                self.permuter(k, i)  # essayer l'objet
                if capa_restante < listobj[k]:  # la boite ouverte n'est pas suffisante
                    # ouvrir une nouvelle boite
                    b = bcount + 1
                    ca = c - (listobj[k])
                else:  # mettre l'objet dans la boite ouverte
                    b = bcount
                    ca = capa_restante - listobj[k]

                s = sumwts - listobj[k]
                # calcul des bornes L1,L2
                bound = b + (math.ceil((s - ca) / c))
                bound2 = b + math.ceil(self.Bound_L2(k + 1))
                # print(bound2)
                if (bound < optcost) and (bound2 < optcost):
                    kk = k + 1
                    self.packBins_BBA(kk, s, b, ca)
                self.permuter(k, i)  # remettre l'objet

        return self.optlist

    # FONCTION QUI APPEL PACKBIN ET RETOURNE LA SOLUTION + LE TEMPS DEXECUTION
    def run_BBA(self, N, C, list):

        sumwts = sum(list)
        bins = 1
        self.init(N, C, list)
        self.packBins_BBA(0, sumwts, bins, C)  # start at index 0
        opt = self.optcost
        lis = self.optlist
        return opt, lis

    def BBA2SOL(self,list,c):
        bins = [[]]
        for objet in list:
            done= False
            for b in bins:
                if (c - sum(b)) >= objet:  # espace suffisant pour objet dans bin
                    b.append(objet)
                    done=True
                    break
            if not done: 
                bins.append([objet])
        return bins
