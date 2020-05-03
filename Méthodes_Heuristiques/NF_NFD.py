# Next-Fit algorithm
def nextfit(weight, c):
    res = 0
    rem = c
    sol=[]
    for i in range(len(weight)):
        if rem >= weight[i]:
            rem = rem - weight[i]

        else:
            res += 1
            rem = c - weight[i]
        sol.append([weight[i], res])
    return (res+1,sol)

# Next-Fit Decreasing algorithm
def next_fit_dec(list_items,max_size):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    list_items.sort(reverse=True)

    # Apply first-fit algorith
    return(nextfit(list_items,max_size))
