from RS_F import RS
from AG import main
from AG import solution
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
    rs= RS()
    nb ,result= rs.RS(n,c,list,bins)

    return nb, result

"""
n = 5
c = 10
list = [1, 1, 9, 4, 9]
hrh_ag_rs(n,c,list)
"""