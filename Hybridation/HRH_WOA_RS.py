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
        if Sol[-1].capacite_restante() >= liste[sol[i]].weight:
            Sol[-1].ranger_obj(liste[sol[i]])
        else:
            Sol.append(Model.Bin(len(Sol), c))
            Sol[-1].ranger_obj(liste[sol[i]])

    print("\tWOA: {} ".format(nb))

    """execute RS"""
    rs = RS()
    nb,result= rs.RS(n,c,list,Sol)
    print("\tWOA_RS: {}".format(nb))

"""
n=5
c=10
list=[1,9,1,4,9]
(hrh_woa_rs(n,c,list))
"""