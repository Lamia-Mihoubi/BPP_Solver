from Méta_Heuristiques.localSearch import localsearch
import Instances_reader
import time
import os
from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Hybridation import HLRH_AG
from Méta_Heuristiques.Recuit_Sim import RS

rs = RS()
print("__________CLASSE 01 ________________")
for filename in os.listdir("C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe1plus"):
    if filename.endswith(".txt") :
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe1plus" + "\\" + filename)
        print(filename)
        #opt = get_opt_sol(1, filename)
        #print("\tSolution {}".format(opt))
        t_exec=time.time()
        sol = HLRH_AG.AG_hyb1(n,c,list)
        t_exec=time.time()-t_exec
        print("\tTexec: {}".format(t_exec))



print("__________CLASSE 02 ________________")

for filename in os.listdir("C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe2plus"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe2plus" + "\\" + filename)
        print(filename)
        opt = get_opt_sol(2, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HLRH_AG.AG_hyb1(n,c,list)
        t_exec = time.time() - t_exec
        print("\tTexec: {}".format(t_exec))

print("__________CLASSE 03 ________________")
for filename in os.listdir("C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe3"):
    if filename.endswith(".txt") and filename.startswith("H"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe3" + "\\" + filename)
        print(filename)
        opt = get_opt_sol(3, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HLRH_AG.AG_hyb1(n,c,list)
        t_exec = time.time() - t_exec
        print("\tTexec: {}".format(t_exec))