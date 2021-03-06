from Méta_Heuristiques.localSearch import localsearch
import Instances_reader
import time
import os
from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Hybridation import HRH_AG_RS
from Méta_Heuristiques.Recuit_Sim import RS
from Méthodes_Heuristiques import FF_FFD

rs = RS()

print("__________CLASSE 01 ________________")
for filename in os.listdir("C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe1plus"):
    if filename.endswith(".txt") :
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe1plus" + "/" + filename)
        print(filename)
        opt = get_opt_sol(1, filename)
        print("\tSolution {}".format(opt))
        t_exec=time.time()
        sol = HRH_AG_RS.hrh_ag_rs(n,c,list)
        t_exec=time.time()-t_exec
        print("\tTexec: {}".format(t_exec))



print("__________CLASSE 02 ________________")

for filename in os.listdir("C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe2plus"):
    if filename.endswith(".txt")  :
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\BACHI\\PycharmProjects\\OPT_PROJET\\BPP_Solver\\Instances_scholl\\classe2plus" + "/" + filename)
        print(filename)
        opt = get_opt_sol(2, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HRH_AG_RS.hrh_ag_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\tTexec: {}".format(t_exec))

print("__________CLASSE 03 ________________")
for filename in os.listdir("/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3"):
    if filename.endswith(".txt") and filename.startswith("H"):
        n, c, list = Instances_reader.ReadInstance(
            "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3" + "/" + filename)
        print(filename)
        opt = get_opt_sol(3, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HRH_AG_RS.hrh_ag_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\tTexec: {}".format(t_exec))
