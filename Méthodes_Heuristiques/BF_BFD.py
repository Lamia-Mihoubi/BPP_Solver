def bestFit(weight, n, c):
    # Initialize result (Count of bins)
    res = 0
    sol=[]
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0] * n
    # Place items one by one
    for i in range(n):

        # Find the first bin that can accommodate
        # weight[i]
        j = 0;

        # Initialize minimum space left and index
        # of best bin
        min = c + 1
        bi = 0

        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):
                bi = j

                min = bin_rem[j] - weight[i]

            # If no bin could accommodate weight[i],
        # create a new bin
        if (min == c + 1):
            bin_rem[res] = c - weight[i]
            sol.append([weight[i], res])
            res += 1
        else:  # Assign the item to best bin
            bin_rem[bi] -= weight[i]
            sol.append([weight[i], bi])
    return (res,sol)

# Best-fit Decreasing Algorithm
# Sort values into decreasing order.
# Then apply best-fit algorithm.
def best_fit_dec(list_items, n,max_size):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    list_items.sort(reverse=True)

    # Apply first-fit algorith
    return(bestFit(list_items, n,max_size))

