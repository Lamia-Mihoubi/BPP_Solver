from BF_F import bestFit
# Best-fit Decreasing Algorithm
# Sort values into decreasing order.
# Then apply best-fit algorithm.
def best_fit_dec(N, C, liste):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    liste.sort(reverse=True)

    # Apply first-fit algorith
    return(bestFit(N, C, liste))