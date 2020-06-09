import Instances_reader
import time
import os
from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Hybridation import HRH_WOA_RS
from Méta_Heuristiques.Recuit_Sim import RS

rs = RS()

print("__________CLASSE 01 ________________")
for filename in os.listdir("/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe1"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe1" + "/" + filename)
        print(filename)
        opt = get_opt_sol(1, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HRH_WOA_RS.hrh_woa_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\t Texec: {}".format(t_exec))

print("__________CLASSE 02 ________________")

for filename in os.listdir("/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe2"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe2" + "/" + filename)
        print(filename)
        opt = get_opt_sol(2, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HRH_WOA_RS.hrh_woa_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\t Texec: {}".format(t_exec))

print("__________CLASSE 03 ________________")
for filename in os.listdir("/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3"):
    if filename.endswith(".txt") and filename.startswith("H"):
        n, c, list = Instances_reader.ReadInstance(
            "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3" + "/" + filename)
        print(filename)
        opt = get_opt_sol(3, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = HRH_WOA_RS.hrh_woa_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\t Texec: {}".format(t_exec))
