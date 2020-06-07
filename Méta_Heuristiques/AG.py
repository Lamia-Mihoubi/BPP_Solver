import numpy as np
import heapq
import random
from Model import Bin
from Model import Objet

crossOverProb = 85  # 0.85 cross-over probability, 85% chance
mutationProb = 10  # 0.1 mutation probability, 10% chance


def Chromosome(object):
    def __init__(self, liste):  # liste des gènes
        self._chromosome = liste[1:]
        self._n = liste[0]  # nombre de boites

    @property
    def chromosome(self):  # Retourne le nom de l'objet.
        return self._chromosome

    @property
    def solution(self):  # retourne la liste des boites et leurs objets
        liste = self._chromosome
        cell0 = liste[0]
        n = len(liste) - 1  # la longueur du chromosome sans la cellule 0
        resultat = []
        for j in range(2 * n):
            resultat.append([])
        liste = copy.deepcopy(liste[1:])  # elimination de la cellule0
        lastB = 1  # compte le nombre de boites utilisées
        for i in range(n):
            c = liste[i]  # numero du gène
            a = (c + 1) % n
            b = int((c + 1) / n)
            if a == 0:
                # print("objet{}, boite{}".format(i+1,b))
                resultat[b].append(i + 1)
                if b > lastB:
                    lastB = b
            else:
                resultat[b + 1].append(i + 1)
                if b > lastB:
                    lastB = b
            # print("objet{}, boite{}".format(i+1,b+1))
        liste1 = [x for x in resultat if x != []]  # elimination es boites vides

        return liste1, len(
            liste1)  # lastb+1 = nombre de boites utilisée #la listee : liste des boites avec leurs objets dedans


def renameItems(liste):
    listeItems = []
    for i in range(len(liste)):
        item = Objet(int(i + 1), int(liste[i]))
        listeItems.append(item)
    return listeItems


def first_fit(list_items, max_size):
    """ Returns list of bins with input items inside. """
    list_bins = []
    list_bins.append(Bin(1, max_size))  # Add first empty bin to list

    cptBins = 1
    for item in list_items:
        # Go through bins and try to allocate
        alloc_flag = False

        for bin in list_bins:
            if bin.total_weight + item.weight <= max_size:
                bin.ranger_obj(item)
                alloc_flag = True
                break

        # If item not allocated in bins in list, create new bin
        # and allocate it to it.
        if alloc_flag == False:
            cptBins += 1
            newBin = Bin(cptBins, max_size)
            newBin.ranger_obj(item)
            list_bins.append(newBin)

    # Turn bins into list of items and return
    list_items = []
    for bin in list_bins:
        list_items.append(bin.get_objects)

    return (list_items), len(list_items)  # nombre de boites


def itemsInBox(liste):
    # donne l'emplacement de chaque objet
    boxes = []
    items = []
    for i in range(len(liste)):
        # items =[]
        for j in range(len(liste[i])):
            string = str(liste[i][j])[1:-2]
            number = string.split(',')[0]
            weight = string.split(',')[1]
            # thing = str(str(i)+','+number+','+str(j))
            thing = str(number + ',' + str(i + 1) + ',' + weight + ',' + str(
                j))  # thing = num_objet,num_boite,weight, pos_boite
            items.append(thing)
        # boxes.append(items)
    return items  # liste des objet sformatés selon leurs boites et leurs positions dans les boites


def toChromosome(liste,
                 n):  # liste dont chaque index= num boite, et liste[index] contient les nums des objets contenus dans la boite
    # n : nombre de boites utilisée
    chromosome = []
    chromosome.append(n)
    for i in range(1, len(liste) + 1):
        chromosome.append(0)
    number = len(liste)  # nombre d'objets
    lastIndex = 1
    lastBoite = 1
    for i in range(len(liste)):  # chaque objet
        string = str(liste[i])
        item = int(string.split(',')[0])
        boite = int(string.split(',')[1])
        weight = int(string.split(',')[2])
        pos = int(string.split(',')[3])
        if int(boite) == lastBoite:
            chromosome[int(item)] = lastIndex + int(pos)
            lastIndex = lastIndex + pos
            lastBoite = int(boite)
        else:
            chromosome[int(item)] = lastIndex + number
            lastIndex = lastIndex + number
            lastBoite = int(boite)

    return chromosome


def chromoTo(liste, n):
    chrom = []
    for i in range(len(liste)):
        chrom.append([])
    for i in range(len(liste)):  # chaque objet
        string = str(liste[i])
        item = int(string.split(',')[0])
        boite = int(string.split(',')[1])
        weight = int(string.split(',')[2])
        pos = int(string.split(',')[3])
        chrom[item - 1] = (boite - 1) * len(liste) + pos
    ch = []
    ch.append(n)
    for i in chrom:
        ch.append(i)
    return ch


def solution(liste):  # retourne la liste des boites et leurs objets
    # la liste en entrée est tout le chromosome avec la cellule zero
    cell0 = liste[0]
    n = len(liste) - 1  # la longueur du chromosome sans la cellule 0
    resultat = []
    for j in range(2 * n):
        resultat.append([])
    liste = copy.deepcopy(liste[1:])  # elimination de la cellule0
    lastB = 1  # compte le nombre de boites utilisées
    for i in range(n):
        c = liste[i]  # numero du gène
        a = (c + 1) % n
        b = int((c + 1) / n)
        if a == 0:
            # print("objet{}, boite{}".format(i+1,b))
            resultat[b].append(i + 1)
            if b > lastB:
                lastB = b
        else:
            resultat[b + 1].append(i + 1)
            if b > lastB:
                lastB = b
            # print("objet{}, boite{}".format(i+1,b+1))
    liste1 = [x for x in resultat if x != []]  # elimination es boites vides

    return liste1, len(
        liste1)  # lastb+1 = nombre de boites utilisée #la listee : liste des boites avec leurs objets dedans


import copy


def generation_ff(listeItems, c, popSize):
    population = []
    longueur = len(listeItems)
    listeItems1 = copy.deepcopy(listeItems)
    # popSize=int((2**(longueur))/(2**(longueur-5)))
    for i in range(popSize):
        liste1 = renameItems(listeItems1)
        liste2, n = first_fit(liste1, c)

        # ------représenter la solution par la représentation chromosomique-------
        liste3 = itemsInBox((liste2))
        res = chromoTo(liste3, n)
        # --------------------------------------------------
        population.append(res)
        random.shuffle(listeItems1)
    return population


# remarque le chromosome généré par ff ne contient pas la cellule zero

def selection(k, popSize, population):
    # Selection of parents randomly by K-Way tournament
    parents = []
    while (len(parents) != popSize):
        index = int(random.random() * (len(population) - 1))
        fittestChromosome = population[index]
        for i in range(k):
            index = int(random.random() * (len(population) - 1))
            if (fittestChromosome[0] > population[index][0]):
                fittestChromosome = copy.deepcopy(population[index])
        parents.append(fittestChromosome)
    return parents


def scramble(chromosome):
    liste = copy.deepcopy(chromosome[1:])
    n = len(liste)
    listeIndices = []
    for i in range(n):
        listeIndices.append(i)
    nombreDeGenes = random.randrange(1, int(n / 2))  # le nombre de genes dans le sous-ensemble à permuter
    indicesPermutation = random.sample(listeIndices, nombreDeGenes)  # le sous ensemble des indices des gènes à permuter
    if len(indicesPermutation) != 1:
        indicesPermutés = indicesPermutation.copy()
        random.shuffle(indicesPermutés)  # la liste des indices permutés
        for i in range(n):
            for j in range(len(indicesPermutation)):
                if i == indicesPermutation[j]:
                    liste[i] = liste[indicesPermutés[j]]
        liste.insert(0, 0)
        liste2, nombreDeBoites = solution(liste)
        liste[0] = nombreDeBoites
    else:
        liste = copy.deepcopy(chromosome)
    return liste


def crossOverMutationRate(prob):
    chance = random.randint(0, 100)
    if (prob >= chance):
        return True
    else:
        return False


# Returns a random cross-over point
def getCrossOverPoint(taille):
    point = 0
    while (point == 0):
        point = random.randint(1, taille)
    return point


def crossover_mutation(population, taille, nbElt, listeWeight, c):
    random.shuffle(population)
    newpopulation = []
    index = 1
    while ((index <= len(population)) and (len(newpopulation) != taille)):
        if (index < len(population)):
            pchrom1 = copy.deepcopy(population[index - 1])
            pchrom2 = copy.deepcopy(population[index])
            fchrom1 = []
            fchrom2 = []
            if (crossOverMutationRate(crossOverProb)):
                point = getCrossOverPoint(len(pchrom1))
                for i in range(len(pchrom1)):
                    if (i == 0):
                        fchrom1.append(pchrom1[i])
                        fchrom2.append(pchrom2[i])
                    if (i != 0):
                        if (i <= point):  # Before and up to cross-over point...
                            fchrom1.append(pchrom1[i])
                            fchrom2.append(pchrom2[i])
                        else:  # After cross-over point...
                            fchrom1.append(pchrom2[i])
                            fchrom2.append(pchrom1[i])
                fchrom11, n1 = solution(fchrom1)
                fchrom22, n2 = solution(fchrom2)
                fchrom1[0] = n1
                fchrom2[0] = n2
            else:
                # Else no cross-over
                fchrom1 = copy.deepcopy(pchrom1)
                fchrom2 = copy.deepcopy(pchrom2)
            if (crossOverMutationRate(mutationProb)):
                fchrom111 = scramble(fchrom1)
                fchrom222 = scramble(fchrom2)
            else:
                fchrom111 = copy.deepcopy(fchrom1)
                fchrom222 = copy.deepcopy(fchrom1)
            sol1, n11 = solution(fchrom111)
            stop1 = fitness(sol1, nbElt, listeWeight, c)
            sol2, n22 = solution(fchrom222)
            stop2 = fitness(sol2, nbElt, listeWeight, c)
            if not stop1:
                fchrom111 = copy.deepcopy(pchrom1)
            elif not stop2:
                fchrom222 = copy.deepcopy(pchrom2)
            newpopulation.append(fchrom111)
            newpopulation.append(fchrom222)
        else:
            pchrom1 = copy.deepcopy(population[index - 1])
            fchrom1 = copy.deepcopy(pchrom1)
            if (crossOverMutationRate(mutationProb)):
                fchrom111 = scramble(fchrom1)
            else:
                fchrom111 = copy.deepcopy(fchrom1)
            sol1, n1 = solution(fchrom111)
            stop1 = fitness(sol1, nbElt, listeWeight, c)
            if not stop1:
                fchrom111 = copy.deepcopy(pchrom1)
            newpopulation.append(fchrom111)
        index = index + 2
    return newpopulation


def getCell0(chromosome):
    return chromosome[0]


def fitness(liste, nbElt, listeWeight, c):
    i = 0
    for p in liste:
        i = i + len(p)
    if (i < nbElt):
        return False
    else:
        for o in range(len(liste)):
            w = 0
            for k in range(len(liste[o])):
                w = w + listeWeight[liste[o][k] - 1]
            if w > c:
                return False
        return True


def evaluation(population, listeWeight, c, nb_elt):
    found = False
    j = 0
    listeX = []
    log = []
    listeM = []
    for i in population:
        listeX.append(getCell0(i))
        res, n = solution(i)
        log.append(fitness(res, nb_elt, listeWeight, c))
        j += 1
    for g in range(len(log)):
        if log[g] == True:
            listeM.append(listeX[g])
    indexes = []
    if True in log:
        for k in range(len(listeX)):
            if log[k] == True:
                if listeX[k] == min(listeM):
                    indexes.append(k)
        retour = []
        for a in indexes:
            retour.append(population[a])
        if (len(retour) > 0):
            found = True
        else:
            found = False
            retour = []
    else:
        found = False
        retour = []
    return retour, found


def next_generation(population, popSize, k, n, c, liste):  # le k de selection
    parents = selection(k, popSize, population)
    newpopulation = crossover_mutation(parents, popSize, n, liste, c)
    return newpopulation


def main(nbGen, k, popSize, n, c, liste):  # le k de selection
    # n,c,liste =ReadInstance("N1C1W1_D.txt")
    population = generation_ff(liste, c, popSize)
    bestfit, found = evaluation(population, liste, c, n)
    if found:
        for i in range(nbGen):
            nx_gen = next_generation(population, popSize, k, n, c, liste)
            liste1, found1 = evaluation(nx_gen, liste, c, n)
            if found1:
                if (bestfit[0] > liste1[0]):
                    bestfit = copy.deepcopy(liste1)
            population = copy.deepcopy(nx_gen)
    return bestfit


def countFreq(arr, n):
    visited = [False for i in range(n)]
    indices = []
    counts = []
    for i in range(n):
        if (visited[i] == True):
            continue

        count = 1
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        indices.append(i)
        counts.append(count)
    index_max = [i for i, x in enumerate(counts) if x == max(counts)]
    return arr.index(arr[index_max[0]]), counts[index_max[0]]


# retourne l'indice du premier max cell0 et le max cell0

n = 10
c = 10
list = [1, 1, 9, 4, 9, 7, 3, 2, 2, 9,5]
sol = main(500, 25, 10, n, c, list)
sol1, n1 = solution(sol[0])
print(n1,sol1)
