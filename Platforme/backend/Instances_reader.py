"""
ReadInstance est une fonction qui permet de lire les fichiers des instances qui se trouvent
 dans le dossier "filepath" et retourner :
    n : le nombre d'objets dans l'instance
    c: la capacité de la boîte
    list : une liste de n objets à ranger


"""
import os


def ReadInstance(filepath):
    liste = []
    file1 = open(filepath, 'r')
    n = int(file1.readline())
    c = int(file1.readline())
    for i in range(n):
        obj = file1.readline()
        liste.append(int(obj))
    return n, c, liste

