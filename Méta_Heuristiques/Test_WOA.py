from Méta_Heuristiques.WOA_ import WOA
import Instances_reader
import Instances_generator
import time
import os

liste1 = [] #ratios de N1
liste2 = []
liste3 = []
liste4 = []

print("__________CLASSE 01 ________________")
file = open("Résultats_Scholl_Classe1_avec_solutions.txt", "a")
file.write("===================================================================\n")
indications_class1 = ["N1C1", "N1C2", "N1C3", "N2C1", "N2C2", "N2C3", "N3C1", "N3C2", "N3C3", "N4C1", "N4C2",
                          "N4C3"]
i=0
for filename in os.listdir("C:\\Users\\dell\\PycharmProjects\\BPP_Solver\\Instances_scholl\\classe1"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\dell\\PycharmProjects\\BPP_Solver\\Instances_scholl\\classe1" + "\\" + filename)
        obj_l=Instances_generator.generate_obj_list2(list,n)
        start_time = time.time()
        woa = WOA(obj_l, search_agents_nbr=10)
        sol,nbin=woa.optimize(c)
        t_exec = time.time() - start_time
        file.write(
            filename[0:len(filename)-4] + ":       " + str(t_exec) + "      boites= " + str(nbin) + "       sol=" + str(sol) + "\n")

file.close()


