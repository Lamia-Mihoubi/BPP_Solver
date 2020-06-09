from ILWOA import ILWOA
from statistics import mean, pstdev
import Instances_reader
import Instances_generator
import time
import os

liste1 = []  # ratios de N1
liste2 = []
liste3 = []
liste4 = []


def class1_test(nb_whales=30, max_iter=50, b=1.5, a=4, beta=1.5):
    print("__________CLASSE 01 ________________")
    file = open("Résultats_Scholl_Classe1_ILWOA.txt", "a")
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
    for filename in os.listdir("./Instances_scholl/classe1"):
        if filename.endswith(".txt"):
            n, c, liste = Instances_reader.ReadInstance(
                "./Instances_scholl/classe1" + "/" + filename
            )
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            ilwoa = ILWOA(objects_list=obj_l,capacity=c)
            start_time = time.time()
            nbin,_ = ilwoa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a, beta=beta)
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


def class2_test(nb_whales=30, max_iter=50, b=1.5, a=4, beta=1.5):
    print("__________CLASSE 02 ________________")
    file = open("Résultats_Scholl_Classe2_ILWOA.txt", "a")
    file.write("===========b={0}, a={1}, max_iter={2}, nb_whales={3}============\n".format(b, a, max_iter, nb_whales))
    i = 0
    for filename in os.listdir("./Instances_scholl/classe2"):
        if filename.endswith(".txt"):
            n, c, liste = Instances_reader.ReadInstance(
                "./Instances_scholl/classe2" + "/" + filename
            )
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            ilwoa = ILWOA(objects_list=obj_l,capacity=c)
            start_time = time.time()
            nbin,_ = ilwoa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a, beta=beta)
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


def class3_test(nb_whales=30, max_iter=50, b=1.5, a=4, beta=1.5):
    print("__________CLASSE 03 ________________")
    file = open("Résultats_Scholl_Classe3_ILWOA.txt", "a")
    file.write("===========b={0}, a={1}, max_iter={2}, nb_whales={3}============\n".format(b, a, max_iter, nb_whales))
    i = 0
    for filename in os.listdir("./Instances_scholl/classe3"):
        if filename.endswith(".txt"):
            n, c, liste = Instances_reader.ReadInstance(
                "./Instances_scholl/classe3" + "/" + filename
            )
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            ilwoa = ILWOA(objects_list=obj_l,capacity=c)
            start_time = time.time()
            nbin,_ = ilwoa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a, beta=beta)
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

def exploit_explor_eval(instances=["./Instances_scholl/classe1/N4C2W4_F.txt", "./Instances_scholl/classe2/N1W3B3R3.txt", "./Instances_scholl/classe3/HARD7.txt"],nb_whales=30, max_iter=50, b=1.5, a=4):
    file = open("exploit_explor_eval_ILWOA.txt", "a")
    file.write("===========b={0}, a={1}, max_iter={2}, nb_whales={3}============\n".format(b, a, max_iter, nb_whales))
    i = 0
    for filename in instances:
            n, c, liste = Instances_reader.ReadInstance(filename)
            obj_l = Instances_generator.generate_obj_list2(liste, n)
            ilwoa = ILWOA(objects_list=obj_l,capacity=c)
            _,evals = ilwoa.optimize(nb_whales=nb_whales, max_iter=max_iter, b=b, a=a)
            file.write(
                filename[28 : len(filename) - 4]
                + "       "
                + str(evals)
                + "\n"
            )
         
# exploit_explor_eval(nb_whales=38, max_iter=280, b=7.36, a=20)

print("\n ===============Manual Param Tuning============ \n")
class1_test()
class2_test()
class3_test()

print("\n ===============Param Tuning with IRace============ \n")
print("\n ===============nb_whales=10, max_iter=10, b=1.5, a=4, beta=1.5============ \n")
class1_test(nb_whales=10, max_iter=10, b=1.5, a=4, beta=1.5)
class2_test(nb_whales=10, max_iter=10, b=1.5, a=4, beta=1.5)
class3_test(nb_whales=10, max_iter=10, b=1.5, a=4, beta=1.5)
print("\n ===============b=0.99, a=8, max_iter=391, nb_whales=13, beta=1.51============ \n")
class1_test(b=0.99, a=8, max_iter=391, nb_whales=13, beta=1.51)
class2_test(b=0.99, a=8, max_iter=391, nb_whales=13, beta=1.51)
class3_test(b=0.99, a=8, max_iter=391, nb_whales=13, beta=1.51)
print("\n ===============b=5.43, a=3, max_iter=441, nb_whales=18, beta=0.33============ \n")
class1_test(b=5.43, a=3, max_iter=441, nb_whales=18, beta=0.33)
class2_test(b=5.43, a=3, max_iter=441, nb_whales=18, beta=0.33)
class3_test(b=5.43, a=3, max_iter=441, nb_whales=18, beta=0.33)
'''
print("\n ===============b=8.96, a=10, max_iter=117, nb_whales=30============ \n")
class1_test(b=8.96, a=10, max_iter=117, nb_whales=30)
class2_test(b=8.96, a=10, max_iter=117, nb_whales=30)
class3_test(b=8.96, a=10, max_iter=117, nb_whales=30)
'''
