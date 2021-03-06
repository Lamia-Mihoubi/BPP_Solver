from Méta_Heuristiques.Recuit_Sim import RS
from Méta_Heuristiques.AG import main
from Méta_Heuristiques.AG import solution
import Model
"""in this version we have an hybrid version of AG with Recuit simulé 
the result of AG is ameliorated by a local search (RS) """


def hrh_ag_rs(n, c, list):
    """execute ag"""
    ag = main(n,c,list)
    sol= solution(ag[0])

    """get result and transform it to a list of Bins"""
    bins=[]
    for i in range (sol[-1]):
        bins.append(Model.Bin(i,c))
        for j in range(len(sol[0][i])):
            bins[i].ranger_obj(Model.Objet(sol[0][i][j]-1,list[sol[0][i][j]-1]))
    print("\tAG: {}".format(len(bins)))
    """execute RS"""
    rs= RS()
    nb ,result= rs.RS(n,c,list,bins)
    print("\tAG_RS: {}".format(nb))

    return result

"""
n = 5
c = 10
list = [1, 1, 9, 4, 9]
hrh_ag_rs(n,c,list)
"""