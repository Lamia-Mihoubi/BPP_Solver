import math
import random
import numpy as np
from decimal import *
import itertools

import Instances_generator as gen
from Functions2 import occupency, LOV
import Model


class WOA:
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
        values=[0 for i in range(objects_nb)]
        while i < objects_nb:
            r = random.randint(0,objects_nb-1)
            if(values[r]==0):
                solution.append(r)
                values[r]+=1
                i = i + 1
        return solution

    def rand_init_population(self):
        population = []
        for i in range(self.search_agents_nbr):
            population.append(self.rand_init_sol())
        # removing duplicate solutions:
        population.sort()

        return np.array(list(k for k, _ in itertools.groupby(population)))

    def init_heuristic(self,heuristic):
        pass

    def get_bin_nbr(self,sol,capacity):
        weight_sum = 0.0
        nbr_bins_used = 0
        # calculating the occupency of every bin
        sol_len=len(sol)
        for i in sol:
            # getting the object of indice i
            obj=self.objects[i]
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

        return nbr_bins_used+1


    def optimize(self, nb_whales=50, max_iter=50, b=1.5, a=2):
        self.search_agents_nbr = nb_whales 
        self.max_iter = max_iter
        self.b = b
        self.a = a
        pop = self.rand_init_population()
        eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
        leader_sol=min(eval_sols)
        leader_index = eval_sols.index(leader_sol)
        leaders=[leader_sol]
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
                            D_x_rand = np.absolute(C * x_rand - pop[sol_index])
                            # I have one issue here, what if the result contains some negative values
                            # would I still apply LOV directly on the result vector or should
                            # I constrain the solution or something, they use here lower and upper
                            # bounds to define when is the resulting array out of our search
                            # domaine so do we need to define them too here? and how to do it?

                            pop[sol_index] = self.discretize(x_rand - A * D_x_rand)
                        else:
                            D_leader = np.absolute(
                                C * pop[leader_index] - pop[sol_index]
                            )
                            pop[sol_index] = self.discretize(
                                pop[leader_index] - A * D_leader
                            )

                    else:  # if p >= 0.5
                        dist_to_leader = np.absolute(pop[leader_index] - pop[sol_index])
                        pop[sol_index]= self.discretize(
                            dist_to_leader
                            * math.exp(self.b * l)
                            * math.cos(l * 2 * math.pi)
                            + pop[leader_index]
                        )

            pop = np.unique(pop, axis=0)
            eval_sols = [self.eval_func(s, self.objects, self.capacity) for s in pop]
            leader_sol=min(eval_sols)
            leader_index = eval_sols.index(leader_sol)
            leaders.append(leader_sol)
        return pop[leader_index], self.get_bin_nbr(pop[leader_index],self.capacity)


    
def callWOA(N,C, liste, nb_whales=50,max_iter=50, b=1.5, a=2):
    liste2=[]
    for i in range(len(liste)):
        liste2.append(Model.Objet(i,liste[i]))
        
    woa= WOA(liste2,C)
    sol,nb = woa.optimize(nb_whales=50, max_iter=50, b=1.5, a=2)
        
    Sol=[Model.Bin(0,C)]
    for i in range(len(sol)):
        if Sol[-1].capacite_restante()>= liste2[sol[i]].weight:
            Sol[-1].ranger_obj(liste2[sol[i]])
        else:
            Sol.append(Model.Bin(len(Sol),C))
            Sol[-1].ranger_obj(liste2[sol[i]])
    return nb, Sol
        
    
        