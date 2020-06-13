import math
import random
import numpy as np
from decimal import *

from Model import Objet

def occupency(solution, objects, capacity, k=2):
    # solution must be an array of integers
    weight_sum = 0.0
    occup_i = 0.0
    occup = []
    # calculating the occupency of every bin

    for i in solution :

        occup_i = weight_sum
        # getting the object of indice i
       # obj = next((obj for obj in objects if obj.id() == i), None)

        obj=objects[i]


        if obj != None:
            weight_sum += obj.weight
        else:
            print("obj {0} doesn't exist in list {1} ".format(i, objects))
        # if the capacity of the bin is filled
        if (capacity < weight_sum):
            occup.append((occup_i / capacity)**k)
            weight_sum = 0
    return 1- (sum(occup) / len(objects)) 

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
        discrete_sol[theta[i]] = i
    return discrete_sol