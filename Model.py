""""
Dans ce fichier on definit les structures de données à utiliser dans les méthodes
on a 2 classes :
la classe Bin :
    - capacité : entier qui represent la capacité de la boîte
    - objects[]: une liste d'objets , represente l'ensemble d'objets rangés dans cette boîte

La classe Objet:
    - ID : entier unique qui represente l'indice de l'objet dans la liste initiale
    - weight : entier qui represent le poids de l'objet

la solution du bin packing est représentée comme suit :
   - m : nombre min de boîtes utilisées
   - list: une liste de m elements de type Bin

a la fin du ficher vous trouverez en commentaire un exemple qui utilise ces structures pour remplir des boites
"""


class Bin(object):

    def __init__(self, id,capacity):
        """Initialise une boite
        """
        self._id=id
        self._objects = []
        self._capacity = capacity
    def __repr__(self):
        return "(%s,%s)" % (self.occupancy,self._objects)

    def set_id(self,id):
        self._id=id
    @property
    def id(self):  # Retourne la capacité de la boite
        return self._id

    def set_obj(self,objects):
        self._objects=objects
    @property
    def capacity(self):  # Retourne la capacité de la boite
        return self._capacity


    @property
    def total_weight(self):  # Retourne le total des poids des objets dans la boite
        return sum([i.weight for i in self._objects])

    @property
    def occupancy(self):
        return self.total_weight * 100 / self.capacity

    def capacite_restante(self):  # retourne l'espace restant dans la boite
        return self._capacity - self.total_weight

    def ranger_obj(self, item):  # range l'objet dans la boite.
        self._objects.append(item)

    def supprimer_obj(self, objet):  # enleve l'objet de la boite
        self._objects.remove(objet)

    @property
    def get_objects(self):  # retourne une liste des objets rangés dans la boite
        return self._objects


class Objet(object):

    def __init__(self, id, weight):
        self._id = id  # nom de l'objet
        self._weight = weight  # poids de l'objet

    @property
    def id(self):  # Retourne le nom de l'objet.
        return self._id

    @property
    def weight(self):  # Retourne le poids de l'objet
        return self._weight

    def __repr__(self):
        return "(%s,%s) " % (self.id, self.weight)


"""
# exemple de test
n = 5
c = 10
# liste des objets
liste = []
bins = 1  # nombre de boites ouvertes
bin = []  # liste des boites utilisées
bin.append(Bin(c))  # déclarer une boite
for i in range(n):
    liste.append(Objet(i, i + 1))  # i used l'indice+1 as a weight x]
# mettre les objets dans des boites

for i in range(n):
    done = False
    for bix in range(bins):
        if bin[bix].capacite_restante() >= liste[i].weight:  # the object fits in the bin
            bin[bix].ranger_obj(liste[i])  # ranger l'objet dedant
            done = True
            break;  # go to next item
    # if object can't fit in dispo bins
    if not done:
        print(i)
        # create new bin and put the object there
        bins = bins + 1;
        b= Bin(c)
        b.ranger_obj(liste[i])
        bin.append(b)

# liste = [1,2,3,4,5]
# la solution should be 2 bins [1,2,3,4] [5]

# afficher le resultat
i = 0
for b in bin:
    objects = b.get_objects
    print("boite {}".format(i))
    for o in range(len(objects)):
        print(objects[o]._id)
    i = i + 1
"""
