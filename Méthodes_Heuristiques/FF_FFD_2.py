def firstFit(weight, n, c):
    # Initialize result (Count of bins)
    res = 0
    sol=[]
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0] * n
    # Place items one by one
    for i in range(n):
        place=False
        for j in range(res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] -= weight[i]
                sol.append([weight[i], j])
                place=True
                bi=j
                break

            # If no bin could accommodate weight[i],
        # create a new bin
        if (place == False):
            bin_rem[res] = c - weight[i]
            sol.append([weight[i], res])
            res += 1
    return (res,sol)

# Best-fit Decreasing Algorithm
# Sort values into decreasing order.
# Then apply best-fit algorithm.
def first_fit_dec(list_items, n,max_size):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    list_items.sort(reverse=True)

    # Apply first-fit algorith
    return(firstFit(list_items, n,max_size))

