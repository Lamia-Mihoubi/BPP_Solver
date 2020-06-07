from WOA import WOA
import Instances_reader
import Instances_generator
import time
import os

liste1 = []  # ratios de N1
liste2 = []
liste3 = []
liste4 = []


def class1_test(nb_whales=30, max_iter=50, b=1.5, a=4):
    print("__________CLASSE 01 ________________")
    file = open("Résultats_Scholl_Classe1_avec_solutions.txt", "a")
    file.write("===========b={0}, a={1}, max_iter={2}, nb_whales={3}============\n".format(b, a, max_iter, nb_whales))
    indications_class1 = [
        "N1C1",
        "N1C2",
        "N1C3",
        "N2C1",
        "N2C2",
        "N2C3",
        "N3C1",
        "N3C2",
        "N3C3",
        "N4C1",
        "N4C2",
        "N4C3",
    ]
    i = 0
    for filename in os.listdir("../Instances_scholl/classe1"):
        if filename.endswith(".txt"):
            n, c, liste = Instances_reader.ReadInstance(
                "../Instances_scholl/classe1" + "/" + filename
            )
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            woa = WOA(objects_list=obj_l,capacity=c)
            start_time = time.time()
            nbin = woa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a)
            t_exec = time.time() - start_time
            file.write(
                filename[0 : len(filename) - 4]
                + "       "
                + str(t_exec)
                + "      "
                + str(nbin)
                + "\n"
            )
        i = i + 1
    file.close()


def class2_test(nb_whales=30, max_iter=50, b=1.5, a=4):
    print("__________CLASSE 02 ________________")
    file = open("Résultats_Scholl_Classe2_avec_solutions.txt", "a")
    file.write("===========b={0}, a={1}, max_iter={2}, nb_whales={3}============\n".format(b, a, max_iter, nb_whales))
    i = 0
    for filename in os.listdir("../Instances_scholl/classe2"):
        if filename.endswith(".txt"):
            n, c, liste = Instances_reader.ReadInstance(
                "../Instances_scholl/classe2" + "/" + filename
            )
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            woa = WOA(objects_list=obj_l,capacity=c)
            start_time = time.time()
            nbin = woa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a)
            t_exec = time.time() - start_time
            file.write(
                filename[0 : len(filename) - 4]
                + "       "
                + str(t_exec)
                + "      "
                + str(nbin)
                + "\n"
            )
            i = i + 1
    file.close()


def class3_test(nb_whales=30, max_iter=50, b=1.5, a=4):
    print("__________CLASSE 03 ________________")
    file = open("Résultats_Scholl_Classe3_avec_solutions.txt", "a")
    file.write("===========b={0}, a={1}, max_iter={2}, nb_whales={3}============\n".format(b, a, max_iter, nb_whales))
    i = 0
    for filename in os.listdir("../Instances_scholl/classe3"):
        if filename.endswith(".txt"):
            n, c, liste = Instances_reader.ReadInstance(
                "../Instances_scholl/classe3" + "/" + filename
            )
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            woa = WOA(objects_list=obj_l,capacity=c)
            start_time = time.time()
            nbin = woa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a)
            t_exec = time.time() - start_time
            file.write(
                filename[0 : len(filename) - 4]
                + "       "
                + str(t_exec)
                + "      "
                + str(nbin)
                + "\n"
            )
            i = i + 1

    file.close()

print("\n ===============Manual Param Tuning============ \n")
class1_test()
class2_test()
class3_test()
print("\n ===============Param Tuning with IRace============ \n")
print("\n ===============nb_whales=38, max_iter=280, b=7.36, a=20============ \n")
class1_test(nb_whales=38, max_iter=280, b=7.36, a=20)
class2_test(nb_whales=38, max_iter=280, b=7.36, a=20)
class3_test(nb_whales=38, max_iter=280, b=7.36, a=20)
print("\n ===============b=7.64, a=20, max_iter=271, nb_whales=28============ \n")
class1_test(b=7.64, a=20, max_iter=271, nb_whales=28)
class2_test(b=7.64, a=20, max_iter=271, nb_whales=28)
class3_test(b=7.64, a=20, max_iter=271, nb_whales=28)
print("\n ===============b=2.23, a=19, max_iter=93, nb_whales=14============ \n")
class1_test(b=2.23, a=19, max_iter=93, nb_whales=14)
class2_test(b=2.23, a=19, max_iter=93, nb_whales=14)
class3_test(b=2.23, a=19, max_iter=93, nb_whales=14)
print("\n ===============b=8.96, a=10, max_iter=117, nb_whales=30============ \n")
class1_test(b=8.96, a=10, max_iter=117, nb_whales=30)
class2_test(b=8.96, a=10, max_iter=117, nb_whales=30)
class3_test(b=8.96, a=10, max_iter=117, nb_whales=30)
