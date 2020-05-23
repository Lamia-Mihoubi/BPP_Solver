from Méta_Heuristiques.localSearch import localsearch
import Instances_reader
import time
import os
from Méta_Heuristiques.get_opt_sol import get_opt_sol
from Méthodes_Heuristiques.BF_BFD import best_fit_dec
from Méta_Heuristiques.Recuit_Sim import RS

liste1 = []  # ratios de N1
liste2 = []
liste3 = []
liste4 = []
file = open("Ratio_local_search.txt", "a")
file.write("===================================================================\n")

ls = localsearch()
rs = RS()

print("__________CLASSE 01 ________________")
for filename in os.listdir("C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe1"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe1" + "\\" + filename)
        #t_exec = time.time()

        #t_exec = time.time() - t_exec
        opt = get_opt_sol(1, filename)
        t_exec = time.time()
        Zs, liste_obj = best_fit_dec(list, n, c)
        t_exec = time.time() - t_exec
        t_exec2 = time.time()
        SS = ls.ameliorer_Sol(n, c, list)
        rss=len(SS)
        t_exec2 = time.time() - t_exec2
        print(filename)
        file.write(filename+"\n")
        print("\tSolution {}".format(opt))
        file.write("\tSolution {}\n".format(opt))

        # print("Heuristique local search {}".format(len(SS)))
        print("\tBFD {}\t {}".format(Zs,t_exec))
        file.write("\tBFD {}\n".format(Zs,t_exec))
        print("\tLS {}\t {}".format(rss,t_exec2))
        file.write("\tLS {}\t {}\n".format(rss,t_exec2))

        if rss < Zs:
            print("Recuit simulé a trouvé une meilleure solution")

        if filename.startswith("N1"):
            liste1.append(len(SS) / int(opt))
        if filename.startswith("N2"):
            liste2.append(len(SS) / int(opt))
        if filename.startswith("N3"):
            liste3.append(len(SS) / int(opt))
        if filename.startswith("N4"):
            liste4.append(len(SS) / int(opt))
        # print("{} :\n optimale={}\n obtenue={}\n T_exec={}".format(filename, opt, len(SS), t_exec))
"""print("ratio Classe1 N1 : {}".format(max(liste1)))
print("ratio Classe1 N2 : {}".format(max(liste2)))
print("ratio Classe1 N3 : {}".format(max(liste3)))
print("ratio Classe1 N4 : {}".format(max(liste4)))
file.write("ratio Classe1 N1 : {}\n".format(max(liste1)))
file.write("ratio Classe1 N2 : {}\n".format(max(liste2)))
file.write("ratio Classe1 N3 : {}\n".format(max(liste3)))
file.write("ratio Classe1 N4 : {}\n".format(max(liste4)))"""
file.write("===================================================================\n")

liste1 = []  # ratios de N1
liste2 = []
liste3 = []
liste4 = []
print("__________CLASSE 02 ________________")

for filename in os.listdir("C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe2"):
    if filename.endswith(".txt"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe2" + "\\" + filename)
        #t_exec = time.time()

        #t_exec = time.time() - t_exec
        rss, sol = rs.RS(n, c, list)
        opt = get_opt_sol(2, filename)
        t_exec=time.time()
        Zs, liste_obj = best_fit_dec(list, n, c)
        t_exec=time.time()-t_exec
        t_exec2 = time.time()
        SS = ls.ameliorer_Sol(n, c, list)
        rss=len(SS)
        t_exec2 = time.time() - t_exec2
        print(filename)
        file.write(filename+"\n")
        print("\tSolution {}".format(opt))
        file.write("\tSolution {}\n".format(opt))

        # print("Heuristique local search {}".format(len(SS)))
        print("\tBFD {}\t {}".format(Zs, t_exec))
        file.write("\tBFD {}\n".format(Zs, t_exec))
        print("\tLS {}\t {}".format(rss, t_exec2))
        file.write("\tLS {}\t {}\n".format(rss, t_exec2))

        if rss < Zs:
            print("Recuit simulé a trouvé une meilleure solution")

        if filename.startswith("N1"):
            liste1.append(len(SS) / int(opt))
        if filename.startswith("N2"):
            liste2.append(len(SS) / int(opt))
        if filename.startswith("N3"):
            liste3.append(len(SS) / int(opt))
        if filename.startswith("N4"):
            liste4.append(len(SS) / int(opt))
        # print("{} :\n optimale={}\n obtenue={}\n T_exec={}".format(filename, opt, len(SS), t_exec))
#print("ratio Classe2 N1 : {}".format(max(liste1)))
#print("ratio Classe2 N2 : {}".format(max(liste2)))
#print("ratio Classe2 N3 : {}".format(max(liste3)))
file.write("ratio Classe2 N1 : {}\n".format(max(liste1)))
file.write("ratio Classe2 N2 : {}\n".format(max(liste2)))
file.write("ratio Classe2 N3 : {}\n".format(max(liste3)))
file.write("===================================================================\n")

liste1 = []

print("__________CLASSE 03 ________________")

for filename in os.listdir("C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe3"):
    if filename.endswith(".txt") and filename.startswith("H"):
        n, c, list = Instances_reader.ReadInstance(
            "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe3" + "\\" + filename)
        #SS = ls.ameliorer_Sol(n, c, list)

        t_exec = time.time()
        Zs, liste_obj = best_fit_dec(list, n, c)
        t_exec = time.time() - t_exec
        opt = get_opt_sol(3, filename)
        #liste1.append(len(SS) / int(opt))
        t_exec2 = time.time()
        SS = ls.ameliorer_Sol(n, c, list)
        rss=len(SS)
        t_exec2 = time.time() - t_exec2
        print(filename)
        file.write(filename+"\n")
        print("\tSolution {}".format(opt))
        file.write("\tSolution {}\n".format(opt))

        # print("Heuristique local search {}".format(len(SS)))
        print("\tBFD {}\t {}".format(Zs, t_exec))
        file.write("\tBFD {}\n".format(Zs, t_exec))
        print("\tRS {}\t {}".format(rss, t_exec2))
        file.write("\tRS {}\t {}\n".format(rss, t_exec2))

        if rss < Zs:
            print("Recuit simulé a trouvé une meilleure solution")

#print("ratio Classe3  : {}".format(max(liste1)))
#file.write("ratio Classe3 : {}\n".format(max(liste1)))
file.write("===================================================================\n")
file.close()
