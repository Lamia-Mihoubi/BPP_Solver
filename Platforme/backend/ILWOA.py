import math
import random
import scipy
import numpy as np
from decimal import *
import itertools
from Chaoticmap import simulation_chaotic

from Functions2 import occupency, LOV
import Model

class ILWOA:
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
    ):
        self.objects = objects_list
        self.capacity = capacity
        self.search_agents_nbr = search_agents_nbr
        self.max_iter = max_iter
        self.b = b
        self.a = a
        self.eval_func = eval_func
        self.discretize = LOV

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
        add = self.init_heuristic(self.capacity)
        population.append(add)
        for i in range(self.search_agents_nbr):
            population.append(self.rand_init_sol())
        # removing duplicate solutions:
        population.sort()

        return np.array(list(k for k, _ in itertools.groupby(population)))

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
            if self.capacity < weight_sum:
                nbr_bins_used += 1
                if obj != None:
                    weight_sum = obj.weight
                else:
                    print("obj {0} doesn't exist in list {1} ".format(i, self.objects))
            elif i == sol[sol_len - 1]:
                nbr_bins_used += 1

        return nbr_bins_used + 1

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

    def optimize(self, nb_whales=50, max_iter=50, b=1.5, a=2, beta=1.5):
        self.search_agents_nbr = nb_whales
        self.max_iter = max_iter
        self.b = b
        self.a = a
        self.search_agents_nbr = nb_whales
        self.max_iter = max_iter
        self.b = b
        self.a = a
        self.beta=beta
        sim=simulation_chaotic(max_iter=self.max_iter,biotic_potential=3.9259904913432475)
        ps=sim.logistic_map(0.63)
        pop = self.rand_init_population()
        eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
        leader_sol=min(eval_sols)
        leader_index = eval_sols.index(leader_sol)
        leaders=[]
        for i in range(self.max_iter):
            a = self.a - i * 2 / self.max_iter
            a2 = -1 + i * (-1) / self.max_iter
            for sol_index in range(pop.shape[0]):
                r1 = random.random()
                r2 = random.random()

                A = 2 * a * r1 - a
                # ILWOA CHANGE:Utiliser la marche aléatoire de levy Pour le C


                l = (a2 - 1) * random.random() + 1
                #ILWOA CHANGE: utiliser chaotic map to initialize p
                p=ps[i]
                #p = random.random()
                if sol_index != leader_index:

                    if p < 0.5:
                        if abs(A) >= 1:
                            rand_leader_index = math.floor(
                                pop.shape[0] * random.random()
                            )
                            x = pop[rand_leader_index]
                            C = sim.levy(np.absolute(
                            x- pop[sol_index]),pop[sol_index] , len(pop[sol_index]), self.beta)
                            D_x_rand = np.absolute(C * x - pop[sol_index])
                            pop[sol_index] = self.discretize(x - A * D_x_rand)
                        else:
                            x = pop[leader_index]
                            C = sim.levy(np.absolute(x - pop[sol_index]),pop[sol_index] , len(x), self.beta)
                            D_leader = np.absolute(
                                C * x - pop[sol_index]
                            )
                            pop[sol_index] = self.discretize(
                                x - A * D_leader
                            )

                    else:  # if p >= 0.5
                        dist_to_leader = np.absolute(pop[leader_index] - pop[sol_index])
                        pop[sol_index]= self.discretize(
                            dist_to_leader
                            * math.exp(self.b * l)
                            * math.cos(l * 2 * math.pi)
                            + pop[leader_index]
                        )
            evaluation=self.eval_func(pop[sol_index],self.objects,self.capacity)


            if(leader_sol>evaluation):
                #print("mut1")
                leader_sol=evaluation
            else :
                mutation=self.mutation(pop[sol_index])
                evaluation = self.eval_func(mutation, self.objects, self.capacity)
                if (leader_sol > evaluation):
                   #print("mut2")
                   pop[sol_index]=mutation
                   leader_sol=evaluation

            pop = np.unique(pop, axis=0)
            eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
            leader_sol=min(eval_sols)
            leader_index = eval_sols.index(leader_sol)
        return pop[leader_index], self.get_bin_nbr(pop[leader_index], self.capacity)

def callILWOA(N,C, liste, nb_whales=50,max_iter=50, b=1.5, a=2, beta=1.5):
    liste2=[]
    for i in range(len(liste)):
        liste2.append(Model.Objet(i,liste[i]))
        
    ilwoa= ILWOA(liste2,C)
    sol,nb = ilwoa.optimize(nb_whales=50, max_iter=50, b=1.5, a=2, beta=1.5)
        
    Sol=[Model.Bin(0,C)]
    for i in range(len(sol)):
        if Sol[-1].capacite_restante()>= liste2[sol[i]].weight:
            Sol[-1].ranger_obj(liste2[sol[i]])
        else:
            Sol.append(Model.Bin(len(Sol),C))
            Sol[-1].ranger_obj(liste2[sol[i]])
    return nb, Sol