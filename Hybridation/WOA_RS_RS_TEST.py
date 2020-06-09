import Instances_reader
import time
import os
from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Hybridation import WOA_RS_RS
from Méta_Heuristiques.Recuit_Sim import RS

rs = RS()


print("__________CLASSE 01 ________________")
for filename in os.listdir("C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe1"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe1" + "\\" + filename)
        print(filename)
        opt = get_opt_sol(1, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = WOA_RS_RS.woa_rs_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\t Texec: {}".format(t_exec))

print("__________CLASSE 02 ________________")

for filename in os.listdir("C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe2"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe2" + "\\" + filename)
        print(filename)
        opt = get_opt_sol(2, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = WOA_RS_RS.woa_rs_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\t Texec: {}".format(t_exec))

print("__________CLASSE 03 ________________")
for filename in os.listdir("C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe3"):
    if filename.endswith(".txt") :
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe3" + "\\" + filename)
        print(filename)
        opt = get_opt_sol(3, filename)
        print("\tSolution {}".format(opt))
        t_exec = time.time()
        sol = WOA_RS_RS.woa_rs_rs(n, c, list)
        t_exec = time.time() - t_exec
        print("\t Texec: {}".format(t_exec))
