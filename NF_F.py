# Next-Fit algorithm
def nextfit(N, C, liste):
    optcost = 0
    rem = C
    N=len(liste)
    optlist=[]
    for i in range(len(liste)):
        if rem >= liste[i]:
            rem = rem - liste[i]

        else:
            optcost += 1
            rem = C - liste[i]
        optlist.append([liste[i], optcost])
        optlist1=sorted(optlist, key = lambda x: int(x[1]))
    liste_box=[]
    box=[]
    second=0
    last=0
    for j in range(len(optlist1)) :
        item=optlist1[j]
        second=item[1]
        if second != last :
            liste_box.append(box)
            box=[]
            box.append(item[0])
            last=second
            if j == len(optlist1)-1 :
                liste_box.append(box)
        else :
            box.append(item[0])
            last=second
            if j == len(optlist1)-1 :
                liste_box.append(box)
    return (optcost+1,liste_box)