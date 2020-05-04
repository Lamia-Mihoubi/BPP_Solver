"""
BPP_Solver : la classe main du projet , d'ici on peut appeler les differentes méthodes implementées, pour résoudre
une instance du Bin packing problem
un exemple d'utilisation est donnée à la fin du fichier

la méthode solve instances permet de résoudre un ensemble d'instances par les méthodes implementées
il suffit de donner en entrées le chemin vers les fichiers d'instances, ansi que mettre à True le booléen correspodant
à la/les méthodes qu'on veut executer 
"""
import os

from Exact_methods.BB import run_BB
from Exact_methods.Exhaustive import run_exhaustive
from Exact_methods.BBA import run_BBA
from Exact_methods.DP import run_DP
from Instances_reader import ReadInstance
from Méthodes_Heuristiques.MH import run_heuristiques

class BPP_Solver:
    # methode qui résout l'ensemble d'instances qui se trouvent dans le dossier "file path"
    # en utilisant les methodes qui sont à True dans les paramètres
    # elle retourne les solutions dans l'ordre des parametres qui sont à True
    def solve_instances(self, filepath, bb=False, bba=False, dp=False, exh=False):

        solutions = []
        directory = filepath
        i = 0
        for filename in os.listdir(directory):

            problem = BPP_Solver()
            if filename.endswith(".txt"):
                n, c, list= ReadInstance(directory + "\\" + filename)
                list.sort(reverse=True)
                solutions.append([])
                if bb: solutions[i].append(BPP_Solver.bb_solver(problem, n, c, list))
                if bba: solutions[i].append(BPP_Solver.bba_solver(problem, n, c, list))
                if dp: solutions[i].append(BPP_Solver.dp_solver(problem, n, c, list))
                if exh: solutions[i].append(BPP_Solver.exhaustive_solver(problem, n, c, list))

                i = i + 1
        return solutions
    def solve_instances_heuristiques(self, filepath, nf=False, nfd=False, ff=False, ffd=False, bf=False, bfd=False):
        solutions = []
        directory = filepath
        i = 0
        for filename in os.listdir(directory):

            problem = BPP_Solver()
            if filename.endswith(".txt"):
                n, c, list= ReadInstance(directory + "/" + filename)
                list.sort(reverse=True)
                solutions.append([])
                if nf: solutions[i].append(BPP_Solver.NF_solver(problem, n, c, list))
                if nfd: solutions[i].append(BPP_Solver.NFD_solver(problem, n, c, list))
                if ff: solutions[i].append(BPP_Solver.FF_solver(problem, n, c, list))
                if ffd: solutions[i].append(BPP_Solver.FFD_solver(problem, n, c, list))
                if bf: solutions[i].append(BPP_Solver.BF_solver(problem, n, c, list))
                if bfd: solutions[i].append(BPP_Solver.BFD_solver(problem, n, c, list))
                i = i + 1
        return solutions
    # the method for solving the BPP using BB:
    def bb_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_BB(nbrItems, binSize, itemWeights)
        return optBinNbr, liste, t_exec

    # the method for solving the BPP using BBA (amelioarted):
    def bba_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_BBA(nbrItems, binSize, itemWeights)
        return optBinNbr, liste, t_exec

    # the method for solving the BPP using DP:
    def dp_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_DP(nbrItems, binSize, itemWeights)
        return optBinNbr, liste, t_exec

    # the method for solving the BPP using Exhaustive search:
    def exhaustive_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_exhaustive(nbrItems, binSize, itemWeights)
        return optBinNbr, liste, t_exec

    # the method for solving the BPP using NF:
    def NF_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_heuristiques(nbrItems, binSize, itemWeights,0)
        return optBinNbr, liste, t_exec
    # the method for solving the BPP using NFD:
    def NFD_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_heuristiques(nbrItems, binSize, itemWeights,1)
        return optBinNbr, liste, t_exec
    # the method for solving the BPP using FF:
    def FF_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_heuristiques(nbrItems, binSize, itemWeights,2)
        return optBinNbr, liste, t_exec
    # the method for solving the BPP using FFD:
    def FFD_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_heuristiques(nbrItems, binSize, itemWeights,3)
        return optBinNbr, liste, t_exec
    # the method for solving the BPP using BF:
    def BF_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_heuristiques(nbrItems, binSize, itemWeights,4)
        return optBinNbr, liste, t_exec
    # the method for solving the BPP using BFD:
    def BFD_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr, liste, t_exec = run_heuristiques(nbrItems, binSize, itemWeights,5)
        return optBinNbr, liste, t_exec
    # the method for solving the BPP using WOA:
    def WOA_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr = 0
        itemsDist = dict()  # the structure of the dictionary: {itemNumber: binNumberContainingIt, ...}
        # code
        return optBinNbr, itemsDist

    # the method for solving the BPP using ILWOA:
    def ILWOA_solver(self, nbrItems, binSize, itemWeights):
        optBinNbr = 0
        itemsDist = dict()  # the structure of the dictionary: {itemNumber: binNumberContainingIt, ...}
        # code
        return optBinNbr, itemsDist


# Exemple d'utilisation
problem = BPP_Solver()
n = 5
c = 20
list = [10, 5, 20, 5, 20]
#print(BPP_Solver.solve_instances(problem, filepath="test", bb=True, bba=False, dp=False, exh=True))
print(BPP_Solver.solve_instances_heuristiques(problem,"Tests", nf=True, nfd=False, ff=False, ffd=False, bf=False, bfd=False))