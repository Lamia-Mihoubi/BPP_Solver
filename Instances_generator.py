"""
Instances generator: est un générateur d'instances du problème bin packing
les poids des objets sont générés aléatoirement en utilisant la fonction "randint"

writeInstance est une fonction qui permet de sauvegarder l'instance générée dans un fichier texte
pour utiliser le generateur , il suffit d'appeler generator en donnant en paramètre

    n : le nombre d'objets
    c: la capacité d'une boite
    grain : utilisée pour generer le seed de la fonction aléatoire,il suffit de donner le même grain
                pour obtenir la même instance
    save[facultatif]: mettre à false si on ne veut pas sauvegarder l'instance ( True par default)
    filepath: le chemin du fichier ou sauvegarder l'instance ( si save=True)

exemple d'utilisation :
n=30
c=15
grain=4
generator(n,c,grain ,"C:\\Users\\winsido\\Desktop\\bigBin_manyItems_4.txt")
"""

from random import seed
from random import randint


def generator(n, c, grain, save=True, filepath=""):
    # n:nbre of items , c: capacity of the bin, so 0 <item weight <= c
    if grain <= c:
        seed(grain)
        liste = []
        for i in range(n):
            liste.append(randint(1, c))
        if save:
            writeInstance(filepath, n, c, liste)
        return liste
    else:
        print("La valeur du grain doit etre inferieure à {}".format(c))


def writeInstance(filepath, n, c, liste):  # writes instance to a file
    file = open(filepath, 'w+')
    file.write(str(n) + '\n')
    file.write(str(c) + '\n')
    for i in range(n):
        file.write(str(liste[i]) + '\n')
    file.close()


