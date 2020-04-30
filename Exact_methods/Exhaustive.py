#Dans ce fichier on implemente une recherche exhaustive pour résoudre
# le problème Bin Packing à une dimension

import time
# DECLARATION DES VARIABLES GLOBALES
n = 0
c = 0
listobj = []
optcost = 0
optlist = []

def permuter(a, b):  # permuter entre 2 objets de la liste
    x = 0
    x = listobj[a]
    listobj[a] = listobj[b]
    listobj[b] = x


def packBins_EXH(k, sumwts, bcount, capa_restante):
    # recherche en profondeur dans un arbre
    # k=ordre de l'objet à etre affecter ( profondeur du noeud)
    # sumwts = somme cumulée des poids des objets restants
    # bcount= somme cumulée du nombre de boîtes utiliséés jusqu'a ce noeud
    # cap_restante= espace libre restant dans la boîte ouverte
    # binPack(0,sumwts,bins,capacity) #on va affecter le 1er objet à une boîte ( et le mettre dans l'indice 0)
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
            optlist = []
            for i in range(n):
                optlist.append(listobj[i])

    else:  # le noeud actuel est un noeud de décision

        for i in range(k, n):  # pour tout objet restant, essayer ce dernier
            permuter(k, i)  # essayer l'objet
            if capa_restante < listobj[k]:  # la boite ouverte n'est pas suffisante
                # ouvrir une nouvelle boite
                b = bcount + 1
                ca = (c) - (listobj[k])
            else:  # mettre l'objet dans la boite ouverte
                b = bcount
                ca = capa_restante - listobj[k]

            s = sumwts - listobj[k]
            kk = k + 1
            packBins_EXH(kk, s, b, ca)  # parcourir les fils
            permuter(k, i)  # remettre l'objet




def run_exhaustive(N,C,list):
    global listobj
    global optcost
    global c
    global n

    start_time = time.time()
    sumwts = sum(list)
    bins = 1
    c = C
    capa_restante = c
    n = N
    listobj = list
    optcost = n
    packBins_EXH(0, sumwts, bins, capa_restante)  # start at index 0
    texec = (time.time() - start_time)

    return optcost, optlist, texec

