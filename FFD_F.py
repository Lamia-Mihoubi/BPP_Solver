# First-fit Algorithm
from Functions import Bin
from FF_F import first_fit
# First-fit Decreasing Algorithm
# Sort values into decreasing order.
# Then apply first-fit algorithm.
def first_fit_dec(N, C, liste):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    liste.sort(reverse=True)
    N=len(liste)
    # Apply first-fit algorith
    return(first_fit(N, C, liste))