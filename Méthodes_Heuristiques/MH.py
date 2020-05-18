import os
import Méthodes_Heuristiques.FF_FFD as ff
import Méthodes_Heuristiques.BF_BFD as bf
import Méthodes_Heuristiques.NF_NFD as nf
import Méthodes_Heuristiques.Functions as fct
import time


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
