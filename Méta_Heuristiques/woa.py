import math
import random
import numpy as np
from decimal import *

from Model import Objet

def eval_func(solution, objects, capacity, k=2):
    weight_sum = 0
    occup_i = 0
    occup = []
    # calculating the occupency of every bin
    for i in solution:
        occup_i = weight_sum
        # getting the object of indice i
        obj = next((obj for obj in objects if obj.id() == i), None)
        if obj != None:
            weight_sum += obj.weight()
        else:
            print("obj {0} doesn't exist in list {1} ".format(i, objects))
        # if the capacity of the bin is filled
        if (capacity < weight_sum):
            occup.append((occup_i / capacity)**k)
            weight_sum = 0
    return 1- (sum(occup) / len(objects)) 

class WhaleOptimization():
    """class implements the whale optimization algorithm as found at
    http://www.alimirjalili.com/WOA.html
    and
    https://doi.org/10.1016/j.advengsoft.2016.01.008
    """
    c = 10;  # capacité
    n = 100;  # nb objets

    def __init__(self, opt_func=eval_func, constraints, nsols, b, a, a_step, list_of_obj, maximize=False):
        self._whales = nsols
        self.objects = list_of_obj
        self._opt_func = opt_func
        self._constraints = constraints
        self._sols = self._init_solutions()
        self._b = b
        self._a = a
        self._a_step = a_step
        self._maximize = maximize

        self._best_solutions = []

    def get_solutions(self):
        """return solutions"""
        return self._sols

    def LOV(continous_sol):
        # getting context float precision for float comparision
        p = getcontext().prec
        # sorting the solution in descending order
        sorted_sol = np.sort(continous_sol)[::-1]
        theta = []
        discrete_sol = np.zeros(shape=(len(continous_sol),), dtype=int)
        # create theta: theta[i]=the order of solution[i]
        for x in continous_sol:
            i = np.where(np.isclose(sorted_sol, x, atol=10**(-p), rtol=10**(-p)))[0][0]

            theta.append(i)
        # create result array
        for i in range(len(theta)):
            discrete_sol[theta[i]] = i + 1
        return discrete_sol

    def optimize(self):
        """solutions randomly encircle, search or attack"""
        ranked_sol = self._rank_solutions()
        best_sol = ranked_sol[0]
        # include best solution in next generation solutions
        new_sols = [best_sol]

        for s in ranked_sol[1:]:
            if np.random.uniform(0.0, 1.0) > 0.5:
                A = self._compute_A()
                norm_A = np.linalg.norm(A)
                if norm_A < 1.0:
                    new_s = self._encircle(s, best_sol, A)
                else:
                    ###select random sol
                    random_sol = self._sols[np.random.randint(self._sols.shape[0])]
                    new_s = self._search(s, random_sol, A)
            else:
                new_s = self._attack(s, best_sol)
            new_sols.append(self._constrain_solution(new_s))

        self._sols = np.stack(new_sols)
        self._a -= self._a_step

    def _init_solutions(self):
        """initialize solutions uniform randomly in space
        """
        solutions = []
        i = 0
        objects_nb = len(self.objects)
        for i in range(self._whales):
            i = 0
            indice = []
            while (i < objects_nb):
                r = random.randint(0, objects_nb - 1)
                if r not in indice:
                    indice.append(r)
                    i = i + 1

            solutions.append(np.take(self.objects, indice))
        solutions = np.stack(solutions)
        return solutions

    def find_nbins(self,solution):
        nbin = 0
        bin = []
        i=0
        bin.append(Model.Bin(nbin,c))
        for i in range(len(solution)):

                if bin[nbin].capacite_restante() >= solution[i].weight:  # the object fits in the bin
                    bin[nbin].ranger_obj(solution[i])  # ranger l'objet deda
                else:

                    nbin = nbin + 1
                    b = Model.Bin(nbin,c)
                    b.ranger_obj(solution[i])
                    bin.append(b)
        return nbin+1, bin

    def _constrain_solution(self, sol):
        """ensure solutions are valid wrt to constraints"""
        constrain_s = []
        for c, s in zip(self._constraints, sol):
            if c[0] > s:
                s = c[0]
            elif c[1] < s:
                s = c[1]
            constrain_s.append(s)
        return constrain_s

    def _rank_solutions(self):
        """find best solution"""
        fitness = self._opt_func(self._sols[:, 0], self._sols[:, 1])
        sol_fitness = [(f, s) for f, s in zip(fitness, self._sols)]

        # best solution is at the front of the list
        ranked_sol = list(sorted(sol_fitness, key=lambda x: x[0], reverse=self._maximize))
        self._best_solutions.append(ranked_sol[0])

        return [s[1] for s in ranked_sol]

    def print_best_solutions(self):
        print('generation best solution history')
        print('([fitness], [solution])')
        for s in self._best_solutions:
            print(s)
        print('\n')
        print('best solution')
        print('([fitness], [solution])')
        print(sorted(self._best_solutions, key=lambda x: x[0], reverse=self._maximize)[0])

    def _compute_A(self):
        r = np.random.uniform(0.0, 1.0, size=2)
        return (2.0 * np.multiply(self._a, r)) - self._a

    def _compute_C(self):
        return 2.0 * np.random.uniform(0.0, 1.0, size=2)

    def _encircle(self, sol, best_sol, A):
        D = self._encircle_D(sol, best_sol)
        return best_sol - np.multiply(A, D)

    def _encircle_D(self, sol, best_sol):
        C = self._compute_C()
        D = np.linalg.norm(np.multiply(C, best_sol) - sol)
        return D

    def _search(self, sol, rand_sol, A):
        D = self._search_D(sol, rand_sol)
        return rand_sol - np.multiply(A, D)

    def _search_D(self, sol, rand_sol):
        C = self._compute_C()
        return np.linalg.norm(np.multiply(C, rand_sol) - sol)

    def _attack(self, sol, best_sol):
        D = np.linalg.norm(best_sol - sol)
        L = np.random.uniform(-1.0, 1.0, size=2)
        return np.multiply(np.multiply(D, np.exp(self._b * L)), np.cos(2.0 * np.pi * L)) + best_sol


def objectiv_function(k, c, n, solution):
    sum = 0
    for b in solution:
        sum += math.pow(b.occupancy, k)
        sum = sum / math.pow(c, k)
    return 1 - (sum / n)


n = 6
c = 10
# liste des objets
liste = []
bins = 1  # nombre de boites ouvertes
bin = []  # liste des boites utilisées
#bin.append(model.Bin(c))  # déclarer une boite
for i in range(n):
    liste.append(Model.Objet(i, i +1))  # i used l'indice+1 as a weight x]
w = WhaleOptimization(None, 0, 10, 0, 0, 0, liste)
# mettre les objets dans des boites
for i in range(len(w._init_solutions())):
    elemt=w._init_solutions()[i]

    print(elemt,w.find_nbins(elemt))
