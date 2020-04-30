# Dans ce fichier on implemente une version améliorée de l'algorithme Branch and Bound pour résoudre
# le problème Bin Packing à une dimension
# l'amelioration consiste a utiliser l'heuristique WFD pour initialiser la solution optimale
# et l'utilisation de la borne L2 pour l'élagage des neouds

import math
import sys
import time
import numpy as np

# DECLARATION DES VARIABLES GLOBALES
n = 0
c = 0
listobj = []
optcost = sys.maxsize
optlist = []


def permuter(a, b):  # permuter entre 2 objets de la liste
    x = 0
    x = listobj[a]
    listobj[a] = listobj[b]
    listobj[b] = x


def wfd():
    global n
    global c
    global listobj
    global optcost
    global optlist

    optlist = listobj
    # ordonne la liste optlist
    optlist.sort(reverse=True)
    bins2 = [0]
    lastbin = 0
    for wix in range(n):  # pour chaque poids d'un objet
        bins2.sort()  # ordonner les boites par ordre decroissant de capacité restante
        done = False
        wt = optlist[wix]  # poids de l'objet wix
        for bix in range(lastbin):  # parcourir les boites ouvertes
            if (wt + bins2[bix]) <= c:  # objet wt peut être ranger dans bix
                bins2[bix] = bins2[bix] + wt  # ranger wt dans bix
                done = True
                break
        if not done:  # l'objet ne peut être ranger dans aucune boîte
            lastbin = lastbin + 1  # ouverture d'une nouvelle boîte
            bins2.append(0)
            bins2[lastbin] = wt  # ranger l'objet dans la nouvelle boîte
    return lastbin + 1


def Bound_L2(k):
    global n
    global c
    global listobj
    global optcost
    global optlist
    # recuperer les poids qui sont inferieurs a C/2
    V = np.unique(listobj)
    V = V[V < (c / 2)]
    L = []

    for j in V:
        # calculer J1 ,J2 et J3
        J1 = []
        J2 = []
        J3 = []
        for i in range(k, n-1):
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


def packBins_BBA(k, sumwts, bcount, capa_restante):

    # recherche en profondeur dans un arbre
    # k=ordre de l'objet à etre affecter ( profondeur du noeud)
    # sumwts = somme cumulée des poids des objets restants
    # bcount= somme cumulée du nombre de boîtes utiliséés jusqu'a ce noeud
    # cap_restante= espace libre restant dans la boîte ouverte
    global optcost
    global optlist
    global listobj
    global n
    global c
    if k == n:  # le noeud actuel est une feuille ( solution exacte)
        # verifier si la solution obtenue est meilleure que la solution optimale
        if bcount < optcost:

            # mettre à jour la solution optimale
            optcost = bcount
            # sauvegarder la solution dans opt_list
            for i in range(n):
                optlist.append(listobj[i])
    else:  # le noeud actuel est un noeud de décision
        for i in range(k, n):  # pour tout objet restant, essayer ce dernier
            permuter(k, i)  # essayer l'objet
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
            bound2 = b + math.ceil(Bound_L2(k + 1))

            if (bound < optcost) and (bound2 < optcost):
                kk = k + 1
                packBins_BBA(kk, s, b, ca)
            permuter(k, i)  # remettre l'objet

    return optlist


# FONCTION QUI APPEL PACKBIN ET RETOURNE LA SOLUTION + LE TEMPS DEXECUTION
def run_BBA(N, C, list):
    global listobj
    global c
    global n
    global optlist
    global listobj
    global optcost
    start_time = time.time()
    sumwts = sum(list)
    bins = 1
    c = C
    capa_restante = c
    n = N
    optlist=[]
    optcost = sys.maxsize

    listobj=[]
    for i in range(n):
        listobj.append(list[i])

    optlist= packBins_BBA(0, sumwts, bins, capa_restante)  # start at index 0
    texec = (time.time() - start_time)

    return optcost, optlist, texec

