from Méta_Heuristiques.Recuit_Sim import RS
from Méta_Heuristiques.WOA_ import WOA
import Model
"""in this version we have an hybrid version of WOA with Recuit simulé 
the result of WOA is ameliorated by a local search (RS) """


def hrh_woa_rs(n, c, list):
    """transform the list of int into a list of Objects"""
    liste=[]
    for i in range(len(list)):
        liste.append(Model.Objet(i,list[i]))
    """execute woa"""
    woa = WOA(liste)
    sol, nb= woa.optimize(c, 0)
    """get result and transform it """
    Sol=[Model.Bin(0,c)]
    for i in range (len(sol)):
        done = False
        for j in range (len(Sol)):
            if Sol[j].capacite_restante()>= liste[sol[i]].weight:
                Sol[j].ranger_obj(liste[sol[i]])
                done = True
                break
        if not done:
            Sol.append(Model.Bin(len(Sol),c))
            Sol[-1].ranger_obj(liste[sol[i]])

    print("\tWOA: {} {}".format(len(Sol),nb))

    """execute RS"""
    rs = RS()
    nb,result= rs.RS_iteratif(n,c,list,Sol)
    print("\tWOA_RS: {}".format(nb))

"""
n=5
c=10
list=[1,9,1,4,9]
(hrh_woa_rs(n,c,list))
"""