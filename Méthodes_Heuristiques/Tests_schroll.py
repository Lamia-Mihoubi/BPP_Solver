import os
import FF_FFD as ff
import BF_BFD as bf
import NF_NFD as nf
import Functions as fct
import time
def ReadInstance(filepath):
    list = []
    file1 = open(filepath, 'r')
    n = int(file1.readline())
    c = int(file1.readline())
    for i in range(n):
        obj = file1.readline()
        list.append(int(obj))
    return n, c, list

def run_heuristiques(n,c,list,f):
    res=0
    sol=[]
    sol1=[]
    if(f==0):
        start_time = time.time()
        res,sol1=nf.nextfit(list, c)
        t_exec = time.time() - start_time
        sol=fct.emballer(sol1,res)
    elif (f==1):
        start_time = time.time()
        res,sol1=nf.next_fit_dec(list, c)
        t_exec = time.time() - start_time
        sol=fct.emballer(sol1,res)
    elif(f==2):
        start_time = time.time()
        sol=ff.first_fit(list,c)
        res=len(sol)
        t_exec = time.time() - start_time
    elif(f==3):
        start_time = time.time()
        sol=ff.first_fit_dec(list,c)
        res=len(sol)
        t_exec = time.time() - start_time
    elif(f==4):
        start_time = time.time()
        res,sol1=bf.bestFit(list,n,c)
        t_exec = time.time() - start_time
        sol=fct.emballer(sol1,res)
    elif(f==5):
        start_time = time.time()
        res,sol1=bf.best_fit_dec(list,n,c)
        t_exec = time.time() - start_time
        sol=fct.emballer(sol1,res)
    
    return (res,sol,t_exec)

def TestMatrix_class1():
    indications_class1 = ["N1C1", "N1C2", "N1C3", "N2C1", "N2C2", "N2C3", "N3C1", "N3C2", "N3C3", "N4C1", "N4C2",
                          "N4C3"]
    methode=["NF","NFD","FF","FFD","BF","BFD"]
    for indication in indications_class1:
        print("______CLASSE 01 ___________")
        directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe1"
        cpt = 0
        sum = 0
        cpt1 = 0
        sum1 = 0
        cpt2 = 0
        sum2 = 0
        cpt3 = 0
        sum3 = 0
        cpt4 = 0
        sum4 = 0
        cpt5 = 0
        sum5 = 0

        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                opt, sol, t_exec= run_heuristiques(n,c,list,0)
                opt1, sol1, t_exec1= run_heuristiques(n,c,list,1)
                opt2, sol2, t_exec2= run_heuristiques(n,c,list,2)
                opt3, sol3, t_exec3= run_heuristiques(n,c,list,3)
                opt4, sol4, t_exec4= run_heuristiques(n,c,list,4)
                opt5, sol5, t_exec5= run_heuristiques(n,c,list,5)
                # use t_exec2, t_exec3 .. if you want to compare different functions
                if t_exec != -1:
                    sum = sum + t_exec
                    cpt = cpt + 1
                if t_exec1 != -1:
                    sum1 = sum1 + t_exec1
                    cpt1 = cpt1 + 1
                if t_exec2 != -1:
                    sum2 = sum2 + t_exec2
                    cpt2 = cpt2 + 1
                if t_exec3 != -1:
                    sum3 = sum3 + t_exec3
                    cpt3 = cpt3 + 1
                if t_exec4 != -1:
                    sum4 = sum4 + t_exec4
                    cpt4 = cpt4 + 1
                if t_exec5 != -1:
                    sum5 = sum5 + t_exec5
                    cpt5 = cpt5 + 1
            # add the same test for other t_exec vars ( create sum2,cpt2...etc)
        print("\n{}:\n".format(indication))
        print("{} : {}\n sol={} bins={}\n".format(methode[0],sum / cpt,sol,opt))
        print("{} : {}\n sol={} bins={}\n".format(methode[1],sum1 / cpt1,sol1,opt1))
        print("{} : {}\n sol={} bins={}\n".format(methode[2],sum2 / cpt2,sol2,opt2))
        print("{} : {}\n sol={} bins={}\n".format(methode[3],sum3 / cpt3,sol3,opt3))
        print("{} : {}\n sol={} bins={}\n".format(methode[4],sum4 / cpt4,sol4,opt4))
        print("{} : {}\n sol={} bins={}\n".format(methode[5],sum5 / cpt5,sol5,opt5))


def TestMatrix_class2():
    indications_class2 = ["N1","N2", "N3", "N4"]
    methode=["NF","NFD","FF","FFD","BF","BFD"]
    for indication in indications_class2:
        print("______CLASSE 02 ___________")
        directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe2"
        cpt = 0
        sum = 0
        cpt1 = 0
        sum1 = 0
        cpt2 = 0
        sum2 = 0
        cpt3 = 0
        sum3 = 0
        cpt4 = 0
        sum4 = 0
        cpt5 = 0
        sum5 = 0

        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                opt, sol, t_exec= run_heuristiques(n,c,list,0)
                opt1, sol1, t_exec1= run_heuristiques(n,c,list,1)
                opt2, sol2, t_exec2= run_heuristiques(n,c,list,2)
                opt3, sol3, t_exec3= run_heuristiques(n,c,list,3)
                opt4, sol4, t_exec4= run_heuristiques(n,c,list,4)
                opt5, sol5, t_exec5= run_heuristiques(n,c,list,5)
                # use t_exec2, t_exec3 .. if you want to compare different functions
                if t_exec != -1:
                    sum = sum + t_exec
                    cpt = cpt + 1
                if t_exec1 != -1:
                    sum1 = sum1 + t_exec1
                    cpt1 = cpt1 + 1
                if t_exec2 != -1:
                    sum2 = sum2 + t_exec2
                    cpt2 = cpt2 + 1
                if t_exec3 != -1:
                    sum3 = sum3 + t_exec3
                    cpt3 = cpt3 + 1
                if t_exec4 != -1:
                    sum4 = sum4 + t_exec4
                    cpt4 = cpt4 + 1
                if t_exec5 != -1:
                    sum5 = sum5 + t_exec5
                    cpt5 = cpt5 + 1
            # add the same test for other t_exec vars ( create sum2,cpt2...etc)

        print("\n{}:\n".format(indication))
        print("{} : {}\n sol={} bins={}\n".format(methode[0],sum / cpt,sol,opt))
        print("{} : {}\n sol={} bins={}\n".format(methode[1],sum1 / cpt1,sol1,opt1))
        print("{} : {}\n sol={} bins={}\n".format(methode[2],sum2 / cpt2,sol2,opt2))
        print("{} : {}\n sol={} bins={}\n".format(methode[3],sum3 / cpt3,sol3,opt3))
        print("{} : {}\n sol={} bins={}\n".format(methode[4],sum4 / cpt4,sol4,opt4))
        print("{} : {}\n sol={} bins={}\n".format(methode[5],sum5 / cpt5,sol5,opt5))


#use it for class3
def TestMatrix_Standard():

    print("______CLASSE 03: (C=100000) ___________")
    methode=["NF","NFD","FF","FFD","BF","BFD"]
    directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3"
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and filename.startswith("HARD"):
            n, c, list = ReadInstance(directory + "/" + filename)
            list.sort(reverse=True)

            opt, sol, t_exec= run_heuristiques(n,c,list,0)
            opt1, sol1, t_exec1= run_heuristiques(n,c,list,1)
            opt2, sol2, t_exec2= run_heuristiques(n,c,list,2)
            opt3, sol3, t_exec3= run_heuristiques(n,c,list,3)
            opt4, sol4, t_exec4= run_heuristiques(n,c,list,4)
            opt5, sol5, t_exec5= run_heuristiques(n,c,list,5)
            print("{} : {}\n sol={} bins={}\n".format(methode[0],t_exec,sol,opt))
            print("{} : {}\n sol={} bins={}\n".format(methode[1],t_exec1,sol1,opt1))
            print("{} : {}\n sol={} bins={}\n".format(methode[2],t_exec2 ,sol2,opt2))
            print("{} : {}\n sol={} bins={}\n".format(methode[3],t_exec3 ,sol3,opt3))
            print("{} : {}\n sol={} bins={}\n".format(methode[4],t_exec4 ,sol4,opt4))
            print("{} : {}\n sol={} bins={}\n".format(methode[5],t_exec5 ,sol5,opt5))
            # print(" {} : BBA:  Texec={}".format(filename, t_exec0))
            #print(" {} : BB:  Texec={}".format(filename, t_exec3))
            #print(" {} : EXH:  Texec={}".format(filename, t_exec2))


TestMatrix_Standard()
