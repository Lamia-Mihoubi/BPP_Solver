from Méthodes_Heuristiques import FF_FFD
import Instances_reader
import time
import os
from Méta_Heuristiques.Recuit_Sim import RS


def TestMatrix_class1():
    indications_class1 = ["N1", "N2", "N3", "N4"]
    methode = ["FFD", "RS"]
    rs = RS()

    print("______CLASSE 01 ___________")
    for indication in indications_class1:
        directory = "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe1"
        cpt = 0
        sum = [0, 0]
        bins = [0, 0]
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = Instances_reader.ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                t_exec = time.time()
                Sol = FF_FFD.first_fit(list,c)
                t_exec = time.time() - t_exec
                Zs = len(Sol)
                t_exec1 = time.time()
                Zs1,Sol1= rs.RS_iteratif(n, c, list)
                t_exec1 = time.time() - t_exec1

                # use t_exec2, t_exec3 .. if you want to compare different functions

                sum[0] = sum[0] + t_exec
                sum[1] = sum[1] + t_exec1
                cpt = cpt + 1
                bins[0] = bins[0] + Zs
                bins[1] = bins[1] + Zs1

        print(indication + " :\n")
        print(methode[0] + ":       \n" + "Texec :"+str(sum[0] / cpt) + "\n NbBins:"+str(bins [0]/cpt))
        print(methode[1] + ":       \n" + "Texec :"+str(sum[1] / cpt) + "\n NbBins:"+str(bins [1]/cpt))


def TestMatrix_class2():
    rs = RS()

    indications_class1 = ["N1", "N2", "N3", "N4"]
    methode = ["RS", "FFD"]

    print("______CLASSE 02 ___________")
    for indication in indications_class1:
        directory = "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe2"
        cpt = 0
        sum = [0, 0]
        bins = [0, 0]
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = Instances_reader.ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                t_exec = time.time()
                Sol = FF_FFD.first_fit(list, c)
                t_exec = time.time() - t_exec
                Zs = len(Sol)
                t_exec1 = time.time()
                Zs1, Sol1 = rs.RS_iteratif(n, c, list)
                t_exec1 = time.time() - t_exec1

                # use t_exec2, t_exec3 .. if you want to compare different functions

                sum[0] = sum[0] + t_exec
                sum[1] = sum[1] + t_exec1
                cpt = cpt + 1
                bins[0] = bins[0] + Zs
                bins[1] = bins[1] + Zs1

        print(indication + " :\n")
        print(methode[0] + ":       \n" + "Texec :" + str(sum[0] / cpt) + "\n NbBins:" + str(bins[0] / cpt))
        print(methode[1] + ":       \n" + "Texec :" + str(sum[1] / cpt) + "\n NbBins:" + str(bins[1] / cpt))


def TestMatrix_class3():
    print("______CLASSE 03 ___________")
    rs = RS()

    directory = "C:\\Users\\BACHI\\Desktop\\OPT_project\\Instances_scholl\\classe2"
    methode = ["RS", "FFD"]
    cpt = 0
    sum = [0, 0]
    bins = [0, 0]
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and filename.startswith("H"):
            n, c, list = Instances_reader.ReadInstance(directory + "//" + filename)
            t_exec = time.time()
            Sol = FF_FFD.first_fit(list, c)
            t_exec = time.time() - t_exec
            Zs = len(Sol)
            t_exec1 = time.time()
            Zs1, Sol1 = rs.RS_iteratif(n, c, list)
            t_exec1 = time.time() - t_exec1

            # use t_exec2, t_exec3 .. if you want to compare different functions

            sum[0] = sum[0] + t_exec
            sum[1] = sum[1] + t_exec1
            cpt = cpt + 1
            bins[0] = bins[0] + Zs
            bins[1] = bins[1] + Zs1

        print(methode[0] + ":       \n" + "Texec :" + str(sum[0] / cpt) + "\n NbBins:" + str(bins[0] / cpt))
        print(methode[1] + ":       \n" + "Texec :" + str(sum[1] / cpt) + "\n NbBins:" + str(bins[1] / cpt))



TestMatrix_class1()
TestMatrix_class2()
TestMatrix_class3()
