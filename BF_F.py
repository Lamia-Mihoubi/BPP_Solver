def bestFit(N, C, liste):
    # Initialize result (Count of bins)
    optcost = 0
    optlist=[]
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0] * N
    # Place items one by one

    for i in range(N):

        # Find the first bin that can accommodate
        # weight[i]
        j = 0;

        # Initialize minimum space left and index
        # of best bin
        min = C + 1
        bi = 0

        for j in range(optcost):
            if (bin_rem[j] >= liste[i] and bin_rem[j] - liste[i] < min):
                bi = j

                min = bin_rem[j] - liste[i]

            # If no bin could accommodate weight[i],
        # create a new bin
        if (min == C + 1):
            bin_rem[optcost] = C - liste[i]
            optlist.append([liste[i], optcost])
            optcost += 1
        else:  # Assign the item to best bin
            bin_rem[bi] -= liste[i]
            optlist.append([liste[i], bi])
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
        
    return (optcost,liste_box)