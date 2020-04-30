"""
Binpacker
========
C'est une solution du binoacking problem basée sur la programmation dynamique.
Item est la classe à laquelle appartienent les objets à ranger, chacun ayant un attribut "poids".
Ce programme va retourner le nombre minimal des boites nécesaires pour ranger tous les objets, ainsi que
le contenu de chaque boite, et le pourcentage d'occupation de son espace

"""
# importer la bibliothèque de gestion des tas "heap"
import heapq
import time
import os
import sys

sys.path.insert(0, os.path.abspath('..'))


# déclarer la classe objet
class Item(object):

    def __init__(self, name, weight):
        self._name = name  # nom de l'objet
        self._weight = weight  # poids de l'objet

    @property
    def name(self):  # Retourne le nom de l'objet.
        return self._name

    @property
    def weight(self):  # Retourne le poids de l'objet
        return self._weight

    def __lt__(self, other):  # retourne vrai si le poids de son objet < poids de "other"
        return self._weight < other._weight

    def __cmp__(self, other):
        """Overload magic method cmp
        Return:
            bool: Ce poids est plus petit que le poids de other.
        """
        return self._weight < other._weight

    def __eq__(self, other):
        """Overload magic method eq
        Return:
            bool: Ce poids est égal au poids de other.
        """
        return self._weight == other._weight


# class Bin
class Bin(object):
    def __init__(self, capacity):
        """Initialise une boite
        """
        # affecte une capacité à la boite crée
        self._items = []
        self._utilization = 0
        self._capacity = capacity

    @property
    def name(self):  # Retourne le nom de la boite.
        return self._name

    @name.setter
    def name(self, name):  # établir le nom de la boite
        self._name = name

    @property
    def capacity(self):  # Retourne la capacité de la boite
        return self._capacity

    @property
    def total_weight(self):  # Retourne le total des poids des objets dans la boite
        return sum([i.weight for i in self._items])

    @property
    def utilization(self):  # Retourne le taux d'utilisation de la boite.
        total_weight = sum([i.weight for i in self._items])
        return round((total_weight / self._capacity) * 100, 2)

    def push(self, item):  # range l'objet dans la boite.
        heapq.heappush(self._items, item)

    def pop(self):  # enleve l'objet de la boite
        return heapq.heappop(self._items)

    def remove(self, name):  # Enlever un objet à partir de la boite en donnant son nom.
        index = 0
        for i, item in enumerate(self._items):
            index = i
            if item.name == name:
                break
        del self._items[index]
        heapq.heapify(self._items)

    def get_items(self, attribute=None, value=None):
        """#Rechercher un objet dans la boite à partir de ses attributs
        si l'attribut, ou la valeur ne sont pas spécifiés, ça va retourner tous les objets de la boite.
        Args:
            attribute (str)[optional]: un des attributs de l'objet.
            value (mixed)[optional]: valueur de l'attribut.
        Returns:
            list: liste des objets.
        """
        if attribute and value:
            return [i for i in self._items if getattr(i, attribute) == value]
        return self._items


class Binpacker(object):
    def __init__(self, capacity):
        """Créer une instance de la classe binpacker.
        Args:
            capacity (int): capacité d'un conteneur.
        """

        self._capacity = capacity
        self._bins = []
        self._items = []

    @property
    def items(self):
        """Retourne les objets.
        Return:
            list: Retourne une liste des objets Item.
        """

        return self._items

    @items.setter
    def items(self, items):
        """Affecte les objets.
        Args:
            list: Une liste des objets Item.
        """
        # la boucle for sert à vérifier si le poids d'un objet dépasse la capacité d'une boite
        for i in items:
            if i.weight > self._capacity:
                raise Exception(
                    'Weight of Item: "{}" exceeds the maximum '
                    'bin capacity: {}.'.format(
                        i.name, self._capacity))
        self._items = items

    @property
    def bins(self):
        """Retourne objet boite.
        """

        return self._bins

    @bins.setter
    def bins(self, bins):
        """Set Bins.
        Args:
            list: liste de boites.
        """

        self._bins = bins

    def get_truth_table(self, capacity, items):
        """Genère la table de vérité.
        """

        m = [
            [True for j in range(capacity + 1)]  # les colonnes
            for i in range(len(items))  # les lignes
        ]
        for index, item in enumerate(items, 1):  # parcourir la liste des objets
            i = index - 1
            for j in range(0, capacity + 1):  # parcourir la boite = les lignes
                if not i:  # si i = 0
                    if j != item.weight and j > 0:
                        m[i][j] = False
                else:
                    if j < item.weight:
                        m[i][j] = m[i - 1][j]
                    else:
                        m[i][j] = m[i - 1][j] or m[i - 1][j - item.weight]
        return m

    def _pick_items(self, truth_table):
        """Choisir les objets à mettre dans la boite
        Args:
            truth_table (list): la table de vérité courante constriute à partir de l'algo Best Fit.
        Returns:
            list: liste des indices des objets choisis.
        """

        k = len(truth_table) - 1  # nombre de lignes - 1
        picked_items_indices = []
        if k >= 0:
            # Prendre le plus lourd subtotal des poids (meilleure utilisation)
            # une boite peut etre remplie.
            j = max([index for index, x in enumerate(truth_table[k]) if x])

            while k >= 0:
                if not k:  # si k ==0
                    if j > 0:
                        picked_items_indices.append(k)
                else:
                    if not truth_table[k - 1][j]:
                        picked_items_indices.append(k)
                        j -= self._items[k].weight
                k -= 1
        return picked_items_indices

    def _move_items_to_bin(self, list_of_items_indices, bin_index):
        """Déplacer les objets vers la boite
        Args:
            list_of_items_indices (list): liste des indices des objets.
            bin_index (int): indice de la boite de destination.
        """

        for i in list_of_items_indices:
            self._bins[bin_index].push(self._items[i])
            del self._items[i]

    def pack_items(self):
        """Ranger les objets dans la(les) boite(s).
        Calcule le nombre min de boites nécessaires, et quel objet
        va dans quelle boite. A la fin de cette méthode, tous les
        objets seront rangés dans des boites. L'état sera mis à jour
        à la demande, c'est à dire que chaque boite peut etre vidée au
        moment où on cherche à la remplir.
        """

        self._items = sorted(self._items)
        # Premièrement, vérifier si l'une des boites déja ouverte pourra
        # accueillir un nouvel objet.
        """for index, old_bin in enumerate(self._bins):
            if old_bin.utilization == 100.00:
                continue
            remaining_space = old_bin.capacity - old_bin.total_weight
            m = self.get_truth_table(remaining_space, self._items)
            picked_items = self._pick_items(m)
            self._move_items_to_bin(picked_items, index)"""

        # S'il nous reste encore des objets à ranger on ouvre une nouvelle boite.
        while len(self._items) > 0:  # tant qu'il nous reste encore un objet à ranger
            m = self.get_truth_table(self._capacity, self._items)
            new_bin = Bin(self._capacity)
            # donner un nom à la nouvelle boite ouverte
            new_bin.name = '[NEW BIN {}]'.format(len(self._bins))
            self._bins.append(new_bin)
            bin_index = len(self._bins) - 1
            picked_items = self._pick_items(m)
            self._move_items_to_bin(picked_items, bin_index)


def convertTuple(tup):
    str = ''.join(tup)
    return str


import itertools


def generateNames(liste):
    with open("../names.txt", "w") as file:
        for L in range(1, len(stuff) + 1):
            for subset in itertools.combinations(stuff, L):
                file.write(convertTuple(subset) + '\n')


stuff = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
generateNames(stuff)


def run_DP(n, c, liste, name_file="names.txt"):
    packer = Binpacker(c)
    packer.items = []
    with open(name_file, "r") as file:
        for i in range(n):
            name = str(file.readline()[:-1])
            weight = liste[i]
            packer.items.append(Item(name, weight))
    start_time = time.time()
    packer.pack_items()
    t_exec = time.time() - start_time
    j = 0
    sol = []
    for i, x in enumerate(packer.bins):
        objets = x.get_items()
        for o in objets:
            sol.append(o.weight)
        j += 1
    return j, sol, t_exec
