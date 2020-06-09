import copy
import math
from statistics import mean, pstdev
import random
import numpy as np
from decimal import *
import itertools
import Model
import Instances_generator as gen
from Méta_Heuristiques.functions import occupency, LOV
import Méta_Heuristiques.Recuit_Sim as RS
def woa_rs_rs(n,c,list):
    """transform the list of int into a list of Objects"""
    liste = []
    for i in range(len(list)):
        liste.append(Model.Objet(i, list[i]))
    """execute woa"""
    woa = WOASA2(liste,c)
    sol, nb = woa.optimize(max_iter=5)
    """get result and transform it """
    Sol = [Model.Bin(0, c)]
    for i in range(len(sol)):
        if Sol[-1].capacite_restante() >= liste[sol[i]].weight:
            Sol[-1].ranger_obj(liste[sol[i]])
        else:
            Sol.append(Model.Bin(len(Sol), c))
            Sol[-1].ranger_obj(liste[sol[i]])

    print("\tWOA_RS: {} ".format(nb))

    """execute RS"""
    rs = RS.RS()
    nb, result = rs.RS(n, c, list, Sol)
    print("\tWOA_RS2: {}".format(nb))

class WOASA2:
    def __init__(
            self,
            objects_list,
            capacity,
            search_agents_nbr=50,
            max_iter=50,
            b=1.5,
            a=2,
            eval_func=occupency,
            discretize=LOV,
            Tinit=30,
            T0=0.1,
            R=1000,
            alpha=0.925
    ):
        self.objects = objects_list
        self.capacity = capacity
        self.search_agents_nbr = search_agents_nbr
        self.max_iter = max_iter
        self.b = b
        self.a = a
        self.eval_func = eval_func
        self.discretize = LOV
        self.Tinit = Tinit
        self.T0 = T0
        self.R = R
        self.alpha = alpha

    def rand_init_sol(self):
        """initialize solutions uniform randomly in space
        """
        objects_nb = len(self.objects)
        i = 0
        solution = []
        values = [0 for i in range(objects_nb)]
        while i < objects_nb:
            r = random.randint(0, objects_nb - 1)
            if (values[r] == 0):
                solution.append(r)
                values[r] += 1
                i = i + 1
        return solution

    def rand_init_population(self):
        population = []
        for i in range(self.search_agents_nbr):
            population.append(self.rand_init_sol())
        # removing duplicate solutions:
        population.sort()

        return np.array(list(k for k, _ in itertools.groupby(population)))

    def get_bin_nbr(self, sol, capacity):
        weight_sum = 0.0
        nbr_bins_used = 0
        # calculating the occupency of every bin
        sol_len = len(sol)
        for i in sol:
            # getting the object of indice i
            obj = self.objects[i]
            if obj != None:
                weight_sum += obj.weight
            else:
                print("obj {0} doesn't exist in list {1} ".format(i, self.objects))
            # if the capacity of the bin is filled
            if capacity < weight_sum:
                nbr_bins_used += 1
                if obj != None:
                    weight_sum = obj.weight
                else:
                    print("obj {0} doesn't exist in list {1} ".format(i, self.objects))
            elif i == sol[sol_len - 1]:
                nbr_bins_used += 1

        return nbr_bins_used

    def create_bins(self, sol):
        bin_list = []
        id_bin = 0
        i = 0
        bin_ = Model.Bin(id_bin, self.capacity)
        for obj in sol:
            #print(obj)
            o = Model.Objet(obj, self.objects[obj].weight)
            if bin_.capacite_restante() >= o.weight:
                bin_.ranger_obj(o)
                if (np.where(sol == obj)[0][0] == len(sol) - 1):
                    bin_list.append(copy.deepcopy(bin_))
            else:  # current object can't fit in current bin
                bin_list.append(copy.deepcopy(bin_))
                id_bin += 1
                bin_.set_id(id_bin)
                bin_.set_obj([])
                bin_.ranger_obj(o)
                if (np.where(sol == obj)[0][0] == len(sol) - 1):
                    bin_list.append(copy.deepcopy(bin_))

        return bin_list

    def optimize(self, nb_whales=30, max_iter=15, b=1.5, a=4, Tinit=20, T0=0.1, R=200, alpha=0.9):

        liste = [o.weight for o in self.objects]

        self.search_agents_nbr = nb_whales
        self.max_iter = max_iter
        self.b = b
        self.a = a
        self.Tinit = Tinit
        self.T0 = T0
        self.R = R
        self.alpha = alpha
        rec_sim = RS.RS()
        pop = self.rand_init_population()
        eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
        leader_sol = min(eval_sols)
        leader_index = eval_sols.index(leader_sol)
        exploit_explor = [[mean(eval_sols), pstdev(eval_sols)]]
        for i in range(self.max_iter):
            a = self.a - i * 2 / self.max_iter
            a2 = -1 + i * (-1) / self.max_iter
            for sol_index in range(pop.shape[0]):
                r1 = random.random()
                r2 = random.random()

                A = 2 * a * r1 - a
                # ILWOA CHANGE:Utiliser la marche aléatoire de levy Pour le C
                C = 2 * r2

                l = (a2 - 1) * random.random() + 1
                p = random.random()
                if sol_index != leader_index:
                    if p < 0.5:
                        if abs(A) >= 1:
                            rand_leader_index = math.floor(
                                pop.shape[0] * random.random()
                            )
                            x_rand = pop[rand_leader_index]
                            S = self.create_bins(x_rand)
                            _, x1 = rec_sim.RS(len(self.objects), self.capacity, liste, S=S)
                            x = rec_sim.RS2WOA(x1)
                            #print(pop[leader_index], len(pop[leader_index]), S, x1, x)
                            D_x_rand = np.absolute(C * x - pop[sol_index])
                            # I have one issue here, what if the result contains some negative values
                            # would I still apply LOV directly on the result vector or should
                            # I constrain the solution or something, they use here lower and upper
                            # bounds to define when is the resulting array out of our search
                            # domaine so do we need to define them too here? and how to do it?

                            pop[sol_index] = self.discretize(x - A * D_x_rand)
                        else:
                            S = self.create_bins(pop[leader_index])
                            _, x1 = rec_sim.RS(len(self.objects), self.capacity, liste, S=S)
                            x = rec_sim.RS2WOA(sol=x1)
                            #print(pop[leader_index], len(pop[leader_index]), S, x1, x)
                            D_leader = np.absolute(
                                C * x - pop[sol_index]
                            )
                            pop[sol_index] = self.discretize(
                                x - A * D_leader
                            )

                    else:  # if p >= 0.5
                        S = self.create_bins(pop[leader_index])

                        _, x1 = rec_sim.RS(len(self.objects), self.capacity, liste, S=S)
                        x = rec_sim.RS2WOA(sol=x1)
                        #print(pop[leader_index], len(pop[leader_index]), S, x1, x)
                        dist_to_leader = np.absolute(x - pop[sol_index])
                        pop[sol_index] = self.discretize(
                            dist_to_leader
                            * math.exp(self.b * l)
                            * math.cos(l * 2 * math.pi)
                            + pop[leader_index]
                        )

            pop = np.unique(pop, axis=0)
            eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
            leader_sol = min(eval_sols)
            leader_index = eval_sols.index(leader_sol)
        return pop[leader_index],self.get_bin_nbr(pop[leader_index], self.capacity)
