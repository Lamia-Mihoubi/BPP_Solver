import os
import sys
import time
import numpy as np
import random
from copy import deepcopy
from BB_F import Binpacker
import RS_F
import NF_F
import NFD_F
import BF_F
import BFD_F
import FF_F
import FFD_F
import Functions
import math
import Model
import Instances_reader
import Model
from get_opt_sol import get_opt_sol
from BFD_F import best_fit_dec
from BF_F import bestFit
from FF_F import first_fit
from FFD_F import first_fit_dec
from NF_F import nextfit
from NFD_F import next_fit_dec
from RS_F import RS
from AG_F import mainAG
from WOA import callWOA
from ILWOA import callILWOA
from DP import DP
from HRH_AG_RS_F import  hrh_ag_rs
import numpy as np
import matplotlib.pyplot as plt

def to_json(cle,tag,optcost,temps,boxes) :
    solution={}
    boites=[]
    for i in range(len(boxes)) :
        boite = boxes[i]
        id_boite = i
        weights=[]
        for j in boite :
            weight={}
            weight['poid'] = j
            weights.append(weight)
        boite={}
        boite={'idbin':id_boite,'objects':weights}
        boites.append(boite)
    resultat={'key':cle,'label':tag,'nb':optcost,'texec':temps,'boites':boites} 
    return resultat

def formate(optcost,optlist) :
    rs=optcost
    SS= optlist
    boxes=[]
    for i in SS :
        boxes.append(i.get_objects)
    list_boxes=[]
    for j in boxes :
        box=[]
        for a in j :
            box.append(a.weight)
        list_boxes.append(box)


    return rs,list_boxes

def switch(dic) :
    variable=[]
    list2 = [int(i) for i in dic['list']]
    n= int(dic['n'])
    c= int(dic['c'])
    if dic['checked_BB'] != 0 :
        start_time_BB = time.time()
        rs = Binpacker()
        nb, listebb= (rs.run_BBA(n, c,list2 ))
        bins= rs.BBA2SOL(listebb,c)      
        
        texec_BB = (time.time() - start_time_BB)
        
        dictio_BB=to_json("BB","Branch and Bound",nb,texec_BB,bins)
        variable.append(dictio_BB)
       #######################################################################
        
    if dic['checked_DP'] != 0 :
        start_time_DP = time.time()
        
        optcost_DP , optlist_DP = DP(n, c, list2)        
        texec_DP = (time.time() - start_time_DP)
        dictio_DP=to_json("DP","Dynamic Programming",optcost_DP,texec_DP,optlist_DP)
        variable.append(dictio_DP)
        ######################################################################
        
    if dic['checked_BF'] != 0 :
        start_time_BF = time.time()
        optcost_BF,optlist_BF=bestFit(n, c, list2)
        
        texec_BF = (time.time() - start_time_BF)
        
        dictio_BF=to_json("BF","Best Fit",optcost_BF,texec_BF,optlist_BF)
        variable.append(dictio_BF)
        ######################################################################
        
    if dic['checked_BFD'] != 0 :
        start_time_BFD = time.time()
        
        optcost_BFD,optlist_BFD=best_fit_dec(n, c, list2)
        
        texec_BFD = (time.time() - start_time_BFD)
        
        dictio_BFD = to_json("BFD","Best Fit Decreasing",optcost_BFD,texec_BFD,optlist_BFD)
        variable.append(dictio_BFD)
        ######################################################################
        
    if dic['checked_FF'] != 0 :
        start_time_FF = time.time()
        
        optcost_FF,optlist_FF=first_fit(n, c, list2)
        
        texec_FF = (time.time() - start_time_FF)
        dictio_FF = to_json("FF","First Fit",optcost_FF,texec_FF,optlist_FF)
        variable.append(dictio_FF)
        ######################################################################
        
    if dic['checked_FFD'] != 0 :
        start_time_FFD = time.time()
        
        optcost_FFD,optlist_FFD=first_fit_dec(n, c, list2)
        
        texec_FFD = (time.time() - start_time_FFD)
        dictio_FFD = to_json("FFD","First Fit Decreasing",optcost_FFD,texec_FFD,optlist_FFD)
        variable.append(dictio_FFD)
        ######################################################################
        
    if dic['checked_NF'] != 0 :
        start_time_NF = time.time()
        
        optcost_NF,optlist_NF=nextfit(n, c, list2)
        
        texec_NF = (time.time() - start_time_NF)
        dictio_NF = to_json("NF","Next Fit",optcost_NF,texec_NF,optlist_NF)
        variable.append(dictio_NF)
        ######################################################################
        
    if dic['checked_NFD'] != 0 :
        start_time_NFD = time.time()
        
        optcost_NFD,optlist_NFD=next_fit_dec(n, c, list2)
        
        texec_NFD = (time.time() - start_time_NFD)
        dictio_NFD = to_json("NFD","Next Fit Decreasing",optcost_NFD,texec_NFD,optlist_NFD)
        variable.append(dictio_NFD)
        ######################################################################
        
    if dic['checked_AG'] != 0 :
        start_time_AG = time.time()
        
        optcost_AG,optlist_AG=mainAG(int(dic['AG_nb_gen']),int(dic['AG_K']),int( dic['AG_popSize']), n, c, list2)
        
        texec_AG = (time.time() - start_time_AG)
        dictio_AG = to_json("AG","Algorithme Génétique",optcost_AG,texec_AG,optlist_AG)
        variable.append(dictio_AG)
        ######################################################################
        
    if dic['checked_WOA'] != 0 :
        start_time_WOA = time.time()
        
        optcost_WOA,optlist_WOA = callWOA(n,c, list2, nb_whales=int(dic['WOA_nb_whales']),max_iter=int(dic['WOA_max_iter']), b=float(dic['WOA_b']), a=float(dic['WOA_a']))
        cost_WOA,liste_WOA = formate(optcost_WOA,optlist_WOA)
        
        texec_WOA = (time.time() - start_time_WOA)
        dictio_WOA = to_json("WOA","Whale Optimization Algorithm",cost_WOA,texec_WOA,liste_WOA)
        variable.append(dictio_WOA)
        ######################################################################
        
    if dic['checked_ILWOA'] != 0 :
        start_time_ILWOA = time.time()
        
        optcost_ILWOA,optlist_ILWOA = callILWOA(n,c, list2,nb_whales=int(dic['ILWOA_nb_agents']),max_iter=dic['ILWOA_max_iter'], b=float(dic['ILWOA_b']), a=float(dic['ILWOA_a']), beta=float(dic['ILWOA_beta']))
        cost_ILWOA,liste_ILWOA = formate(optcost_ILWOA,optlist_ILWOA)
        
        texec_ILWOA = (time.time() - start_time_ILWOA)
        dictio_ILWOA = to_json("ILWOA","Improved Whale Optimization Algorithm",cost_ILWOA,texec_ILWOA,liste_ILWOA)
        variable.append(dictio_ILWOA)
        ######################################################################
        
    if dic['checked_RS'] != 0 :
        start_time_RS = time.time()
        
        classrs = RS()
        optcost_RS,optlist_RS=classrs.RS_iteratif(n, c, list2,R=int(dic['RS_nb_iter']),alpha=float(dic['RS_alpha']))
        
        texec_RS = (time.time() - start_time_RS)
        dictio_RS = to_json("RS","Recuit Simulé",optcost_RS,texec_RS,optlist_RS)
        variable.append(dictio_RS)
        ######################################################################
    if dic['checked_Hyb1'] != 0 :
        start_time_Hyb1 = time.time()
        
        optcost_Hyb1,optlist_Hyb1= hrh_ag_rs(n,c,list2)
        
        texec_Hyb1 = (time.time() - start_time_Hyb1)
        dictio_Hyb1 = to_json("Hyb1","Hybridation HRH AG+RS",optcost_Hyb1,texec_Hyb1,optlist_Hyb1)
        variable.append(dictio_Hyb1)
    ######################################################################
    
    return variable
def gen_graphs(MethodNames,temps,bins):
    height = [3, 12, 5, 18, 45]
    bars = ('A', 'B', 'C', 'D', 'E')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.xticks(y_pos, bars)
    #plt.show()


