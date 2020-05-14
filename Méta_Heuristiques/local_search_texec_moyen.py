from Méta_Heuristiques.localSearch import localsearch
import Instances_reader
import time
import os


def TestMatrix_class1():
    indications_class1 = ["N1C1", "N1C2", "N1C3", "N2C1", "N2C2", "N2C3", "N3C1", "N3C2", "N3C3", "N4C1", "N4C2",
                          "N4C3"]
    methode=["LS"]
    print("______CLASSE 01 ___________")
    for indication in indications_class1:
        directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe1"
        cpt = 0
        sum = 0
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = Instances_reader.ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                t_exec=time.time()
                ls=localsearch()
                Sol = ls.ameliorer_Sol(n,c,list)
                t_exec=time.time()-t_exec
                Zs=len(Sol)
                # use t_exec2, t_exec3 .. if you want to compare different functions
                if t_exec != -1:
                    sum = sum + t_exec
                    cpt = cpt + 1

        file = open("Résultats_local search texec_moyenne_classe1.txt", "a")
        file.write("===================================================================\n")
        file.write(indication+" :\n")
        file.write(methode[0]+":       "+str(sum/cpt)+"\n")
        print(indication+" :\n")
        print(methode[0]+":       "+str(sum/cpt)+"\n")
        file.close()
def TestMatrix_class2():
    indications_class2 = ["N1", "N2", "N3", "N4"]

    methode=["LS"]
    print("______CLASSE 02 ___________")
    for indication in indications_class2:
        directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe2"
        cpt = 0
        sum = 0
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = Instances_reader.ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                t_exec=time.time()
                ls=localsearch()
                Sol = ls.ameliorer_Sol(n,c,list)
                t_exec=time.time()-t_exec
                Zs=len(Sol)
                # use t_exec2, t_exec3 .. if you want to compare different functions
                if t_exec != -1:
                    sum = sum + t_exec
                    cpt = cpt + 1

        file = open("Résultats_local search texec_moyenne_classe2.txt", "a")
        file.write("===================================================================\n")
        file.write(indication+" :\n")
        file.write(methode[0]+": "+str(sum/cpt)+"\n")
        print(indication+" :\n")
        print(methode[0]+": "+str(sum/cpt)+"\n")
        file.close()

def TestMatrix_class3():
    directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3"
    file = open("Résultats_local search texec_classe3.txt", "a")

    for filename in os.listdir(directory):
        if filename.endswith(".txt") and filename.startswith("H"):
            n, c, list = Instances_reader.ReadInstance(directory + "//" + filename)
            t_exec = time.time()
            ls = localsearch()
            SS = ls.ameliorer_Sol(n, c, list)
            t_exec = time.time() - t_exec
            file.write("LS" + ": {}".format(t_exec)+ "\n")
            print(filename + " :\n")
            print("LS" + ": {}".format(t_exec) + "\n")
    file.close()


TestMatrix_class1()
TestMatrix_class2()
TestMatrix_class3()
