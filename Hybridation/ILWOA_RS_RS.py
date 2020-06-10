import copy
import math
from statistics import mean, pstdev
import random
import numpy as np
from decimal import *
import itertools
import Model
import Instances_generator as gen
from Chaoticmap import simulation_chaotic
from Méta_Heuristiques.functions import occupency, LOV
import Méta_Heuristiques.Recuit_Sim as RS



def ilwoa_rs_rs(n,c,list):
    """transform the list of int into a list of Objects"""
    liste = []
    for i in range(len(list)):
        liste.append(Model.Objet(i, list[i]))
    """execute ilwoa"""
    ilwoars = ILWOASA(liste, c)
    sol, nb = ilwoars.optimize(max_iter=50) # change here if you wanna try with less iterations
    """get result and transform it """
    Sol = [Model.Bin(0, c)]
    for i in range(len(sol)):
        if Sol[-1].capacite_restante() >= liste[sol[i]].weight:
            Sol[-1].ranger_obj(liste[sol[i]])
        else:
            Sol.append(Model.Bin(len(Sol), c))
            Sol[-1].ranger_obj(liste[sol[i]])

    print("\tILWOA_RS1: {} ".format(nb))

    """execute RS"""
    rs = RS.RS()
    nb, result = rs.RS(n, c, list, Sol)
    print("\tILWOA_RS2: {}".format(nb))


class ILWOASA:
    def __init__(
            self,
            objects_list,
            capacity,
            search_agents_nbr=50,
            max_iter=50,
            b=1.5,
            a=2,
            beta=1.5,
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

    def init_heuristic(self, c):
        # Initialize result (Count of bins)
        res = 0
        sol = []
        ind_sol = []
        n = len(self.objects)
        # Create an array to store remaining space in bins
        # there can be at most n bins
        bin_rem = [0] * n
        # Place items one by one
        for i in range(n):

            # Find the first bin that can accommodate
            # weight[i]
            j = 0

            # Initialize minimum space left and index
            # of best bin
            min_ = c + 1
            bi = 0

            for j in range(res):
                if (bin_rem[j] >= self.objects[i].weight and bin_rem[j] - self.objects[i].weight < min_):
                    bi = j

                    min_ = bin_rem[j] - self.objects[i].weight

                # If no bin could accommodate weight[i],
            # create a new bin
            if (min_ == c + 1):
                bin_rem[res] = c - self.objects[i].weight
                sol.append([i, res])
                res += 1
            else:  # Assign the item to best bin
                bin_rem[bi] -= self.objects[i].weight
                sol.append([i, bi])

        sol.sort(key=lambda tup: tup[1])
        zipped = sol

        unzipped_object = zip(*zipped)

        unzipped_list = list(unzipped_object)

        return list(unzipped_list[0])

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

        return nbr_bins_used +1

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

    def mutation(self, sol):

        ind1 = random.randint(0, len(sol) - 1)
        ind2 = ind1
        while (ind1 == ind2):
            ind2 = random.randint(0, len(sol) - 1)
        # SWAP
        q = sol[ind2]
        sol[ind2] = sol[ind1]
        sol[ind1] = q

        # Displacement

        init_sub = random.randint(1, len(sol) - 1)
        length_sub = ind1 = random.randint(1, len(sol) - init_sub)
        tomove = sol[init_sub:init_sub + length_sub]
        move_pos = random.randint(0, len(sol) - 1)
        if (init_sub != move_pos):

            if (init_sub > move_pos):
                a1 = sol[0:move_pos]

                a2 = sol[move_pos:init_sub]
                a3 = sol[init_sub + length_sub:len(sol)]
            else:

                a1 = sol[0:init_sub]

                if (init_sub + length_sub < move_pos):
                    a2 = sol[init_sub + length_sub:move_pos]

                    a1 = np.append(a1, a2)

                    a2 = sol[move_pos:len(sol)]
                else:
                    a2 = sol[init_sub + length_sub:len(sol)]
            a1 = np.append(a1, tomove)
            a1 = np.append(a1, a2)
            if (init_sub > move_pos):
                a1 = np.append(a1, a3)
            sol = a1
        # reversion
        init_sub = random.randint(0, len(sol) - 1)
        length_sub = random.randint(1, len(sol) - 1)
        sol[init_sub:init_sub + length_sub] = sol[init_sub:init_sub + length_sub][::-1]

        return sol.astype(int)

    def optimize(self, nb_whales=50, max_iter=50, b=1.5, a=2, beta=1.5, Tinit=20, T0=0.1, R=200, alpha=0.9):
        rec_sim = RS.RS()
        self.search_agents_nbr = nb_whales
        self.max_iter = max_iter
        self.b = b
        self.a = a
        sim = simulation_chaotic(max_iter=self.max_iter, biotic_potential=3.9259904913432475)
        ps = sim.logistic_map(0.63)
        pop = self.rand_init_population()
        eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
        leader_sol = min(eval_sols)
        leader_index = eval_sols.index(leader_sol)
        leaders = []
        for i in range(self.max_iter):
            a = self.a - i * 2 / self.max_iter
            a2 = -1 + i * (-1) / self.max_iter
            for sol_index in range(pop.shape[0]):
                r1 = random.random()
                r2 = random.random()

                A = 2 * a * r1 - a
                # ILWOA CHANGE:Utiliser la marche aléatoire de levy Pour le C

                l = (a2 - 1) * random.random() + 1
                # ILWOA CHANGE: utiliser chaotic map to initialize p
                p = ps[i]
                # p = random.random()
                if sol_index != leader_index:

                    if p < 0.5:
                        if abs(A) >= 1:
                            rand_leader_index = math.floor(
                                pop.shape[0] * random.random()
                            )
                            x_rand = pop[rand_leader_index]
                            S = self.create_bins(x_rand)
                            _, x1 = rec_sim.RS(len(self.objects), self.capacity, [], S=S)
                            x = rec_sim.RS2WOA(x1)
                            C = sim.levy(np.absolute(
                                x - pop[sol_index]), pop[sol_index], len(pop[sol_index]), beta)
                            D_x_rand = np.absolute(C * x - pop[sol_index])
                            pop[sol_index] = self.discretize(x - A * D_x_rand)
                        else:
                            S = self.create_bins(pop[leader_index])
                            _, x1 = rec_sim.RS(len(self.objects), self.capacity, [], S=S)
                            x = rec_sim.RS2WOA(sol=x1)
                            C = sim.levy(np.absolute(x - pop[sol_index]), pop[sol_index], len(x), beta)
                            D_leader = np.absolute(
                                C * x - pop[sol_index]
                            )
                            pop[sol_index] = self.discretize(
                                x - A * D_leader
                            )

                    else:  # if p >= 0.5
                        S = self.create_bins(pop[leader_index])
                        _, x1 = rec_sim.RS(len(self.objects), self.capacity, [], S=S)
                        x = rec_sim.RS2WOA(sol=x1)
                        dist_to_leader = np.absolute(x - pop[sol_index])
                        pop[sol_index] = self.discretize(
                            dist_to_leader
                            * math.exp(self.b * l)
                            * math.cos(l * 2 * math.pi)
                            + pop[leader_index]
                        )
            evaluation = self.eval_func(pop[sol_index], self.objects, self.capacity)

            if (leader_sol > evaluation):
                # print("mut1")
                leader_sol = evaluation
            else:
                mutation = self.mutation(pop[sol_index])
                evaluation = self.eval_func(mutation, self.objects, self.capacity)
                if (leader_sol > evaluation):
                    # print("mut2")
                    pop[sol_index] = mutation
                    leader_sol = evaluation

            pop = np.unique(pop, axis=0)
            eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
            leader_sol = min(eval_sols)
            leader_index = eval_sols.index(leader_sol)
        # print(pop[leader_index])
        return pop[leader_index], self.get_bin_nbr(pop[leader_index], self.capacity)
