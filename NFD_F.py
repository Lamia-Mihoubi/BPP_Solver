from NF_F import nextfit

# Next-Fit Decreasing algorithm
def next_fit_dec(N, C, liste):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    liste.sort(reverse=True)

    # Apply first-fit algorith
    return(nextfit(N, C, liste))
