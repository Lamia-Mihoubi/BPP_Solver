import os
import FF_FFD_2 as ff
import BF_BFD as bf
import NF_NFD as nf
import Functions as fct
import time
from DP import run_DP
from BBA import run_BBA
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
        sol=fct.emballer(sol1,res)
        t_exec = time.time() - start_time
    elif (f==1):
        start_time = time.time()
        res,sol1=nf.next_fit_dec(list, c)
        sol=fct.emballer(sol1,res)
        t_exec = time.time() - start_time
    elif(f==2):
        start_time = time.time()
        res,sol1=ff.firstFit(list,n,c)
        sol=fct.emballer(sol1,res)
        t_exec = time.time() - start_time
    elif(f==3):
        start_time = time.time()
        res,sol1=ff.first_fit_dec(list,n,c)
        sol=fct.emballer(sol1,res)
        t_exec = time.time() - start_time
    elif(f==4):
        start_time = time.time()
        res,sol1=bf.bestFit(list,n,c)
        sol=fct.emballer(sol1,res)
        t_exec = time.time() - start_time
        
    elif(f==5):
        start_time = time.time()
        res,sol1=bf.best_fit_dec(list,n,c)
        sol=fct.emballer(sol1,res)
        t_exec = time.time() - start_time
    
    return (res,sol,t_exec)


def TestMatrix_class1():
    indications_class1 = ["N1C1", "N1C2", "N1C3", "N2C1", "N2C2", "N2C3", "N3C1", "N3C2", "N3C3", "N4C1", "N4C2",
                          "N4C3"]
    methode=["NF","NFD","FF","FFD","BF","BFD"]
    for indication in indications_class1:
        print("______CLASSE 01 ___________")
        directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe1"

        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                opt, sol, t_exec= run_heuristiques(n,c,list,4)
                
                #opt0, sol0, t_exec0= run_BBA(n,c,list)
                # use t_exec2, t_exec3 .. if you want to compare different functions
                
                #if t_exec0 != -1:
                 #   sum0 = sum0 + t_exec0
                  #  cpt0 = cpt0 + 1
            # add the same test for other t_exec vars ( create sum2,cpt2...etc)
                
                if filename.startswith("N1"):
                    file = open("BF_Classe1_N1.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close()
                if filename.startswith("N2"):
                    file = open("BF_Classe1_N2.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close()
                if filename.startswith("N3"):
                    file = open("BF_Classe1_N3.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close()
                if filename.startswith("N4"):
                    file = open("BF_Classe1_N4.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close() 
        


def TestMatrix_class2():
    indications_class2 = ["N1","N2", "N3", "N4"]
    methode=["NF","NFD","FF","FFD","BF","BFD"]
    for indication in indications_class2:
        print("______CLASSE 02 ___________")
        directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe2"
        
        for filename in os.listdir(directory):
            if filename.endswith(".txt") and filename.startswith(indication):
                n, c, list = ReadInstance(directory + "/" + filename)
                # t_exec= temps d'execution de la fonction
                opt, sol, t_exec= run_heuristiques(n,c,list,4)
                #opt0, sol0, t_exec0= run_DP(n,c,list)
                # use t_exec2, t_exec3 .. if you want to compare different functions
                
                #if t_exec0 != -1:
                 #   sum0 = sum0 + t_exec0
                  #  cpt0 = cpt0 + 1
            # add the same test for other t_exec vars ( create sum2,cpt2...etc)
                if filename.startswith("N1"):
                    file = open("BF_Classe2_N1.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close()
                if filename.startswith("N2"):
                    file = open("BF_Classe2_N2.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close()
                if filename.startswith("N3"):
                    file = open("BF_Classe2_N3.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close()
                if filename.startswith("N4"):
                    file = open("BF_Classe2_N4.txt", "a")
                    item=filename.split(".")
                    file.write(item[0]+" "+str(opt)+"\n")
                    file.close() 


#use it for class3
def TestMatrix_Standard():

    print("______CLASSE 03: (C=100000) ___________")
    methode=["NF","NFD","FF","FFD","BF","BFD"]
    directory = "/home/nsarah/Documents/2CS-SIQ3-S2/2019-2020/OPT/TP/GitHub/BPP_Solver/Instances_scholl/classe3"
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and filename.startswith("HARD"):
            n, c, list = ReadInstance(directory + "/" + filename)
            list.sort(reverse=True)

            opt, sol, t_exec= run_heuristiques(n,c,list,4)
            file = open("BF_Classe3_N3.txt", "a")
            item=filename.split(".")
            file.write(item[0]+" "+str(opt)+"\n")
            file.close()
            

TestMatrix_class1()
TestMatrix_class2()
TestMatrix_Standard()
