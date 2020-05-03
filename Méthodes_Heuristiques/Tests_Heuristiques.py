import FF_FFD as ff
import BF_BFD as bf
import NF_NFD as nf
import Functions as fct


print("\n==============EXEMPLE 1==================================================")

weights = [8, 16, 12, 8, 45, 18, 30, 7, 10, 14, 9, 9, 52, 58]
bin_height = 60
n = len(weights);
print("Les poids des objets: ",weights,"\nLe nombre d'objets: ",n,"\nLa capacité d une bin: ", bin_height)
#Next-Fit Algorithm
res,sol=nf.nextfit(weights, bin_height )
print("Algorithme Next Fit :    La solution :", fct.emballer(sol,res),"     Nombre de bins utilisées: " ,res)
#Next-Fit Decreasing Algorithm
res1,sol1=nf.next_fit_dec(weights, bin_height)
print("Algorithme Next Fit Decreasing:    La solution :", fct.emballer(sol1,res),"     Nombre de bins utilisées: " ,res1)
# First-fit Algorithm
ff1=ff.first_fit(weights, bin_height)
print("Algorithme First-Fit: La solution:",ff1,"    Nombre de bins utilisées: ",len(ff1))
ffd=ff.first_fit_dec(weights, bin_height)
# First-fit Decreasing Algorithm
print("Algorithme First-Fit Decreasing: La solution:",ffd,"    Nombre de bins utilisées: ",len(ffd))
#Best Fit Algorithm
n2,l2=bf.bestFit(weights, n, bin_height )
print("Algorithme Best Fit :[item,bin] ",fct.emballer(l2,n2),"     Nombre de bins utilisées: ",n2);
#Best Fit Decreasing Algorithm
n3,l3= bf.best_fit_dec(weights, n, bin_height )
print("Algorithme Best Fit Decreasing: La solution: ",fct.emballer(l3,n3),"     Nombre de bins utilisées: ",n3);
print("=================EXEMPLE2=====================================================")
weights1 = [ 2, 5, 4, 7, 1, 3, 8 ];
c = 10;
n1 = len(weights1);
print("Les poids des objets: ",weights1,"\nLe nombre d'objets: ",n1,"\nLa capacité d une bin: ", c)
print("La solution optimale est de = 3")
#Next-Fit Algorithm
res3,sol3=nf.nextfit(weights1, c )
print("Algorithme Next Fit :    La solution :", fct.emballer(sol3,res3),"     Nombre de bins utilisées: " ,res3)
#Next-Fit Decreasing Algorithm
res4,sol4=nf.next_fit_dec(weights1, c)
print("Algorithme Next Fit Decreasing:    La solution :", fct.emballer(sol4,res4),"     Nombre de bins utilisées: " ,res4)
# First-fit Algorithm
ff1=ff.first_fit(weights1, c)
print("Algorithme First-Fit: La solution:",ff1,"    Nombre de bins utilisées: ",len(ff1))
ffd1=ff.first_fit_dec(weights1, c)
# First-fit Decreasing Algorithm
print("Algorithme First-Fit Decreasing: La solution:",ffd1,"    Nombre de bins utilisées: ",len(ffd1))
#Best Fit Algorithm
n22,l22=bf.bestFit(weights1, n1, c)
print("Algorithme Best Fit : La solution ",fct.emballer(l22,n22),"    Nombre de bins utilisées: ",n22)
#Best Fit Decreasing Algorithm
n4,l4= bf.best_fit_dec(weights1, n1, c)
print("Algorithme Best Fit Decreasing: La solution ",fct.emballer(l4,n4),"     Nombre de bins utilisées: ",n4);
