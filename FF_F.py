# First-fit Algorithm
from Functions import Bin
def first_fit(N, C, liste):
    """ Returns list of bins with input items inside. """
    list_bins = []
    list_bins.append(Bin())  # Add first empty bin to list

    for item in liste:
        # Go through bins and try to allocate
        alloc_flag = False

        for bin in list_bins:
            if bin.sum() + item <= C:
                bin.addItem(item)
                alloc_flag = True
                break

        # If item not allocated in bins in list, create new bin
        # and allocate it to it.
        if alloc_flag == False:
            newBin = Bin()
            newBin.addItem(item)
            list_bins.append(newBin)

    # Turn bins into list of items and return
    liste= []
    for bin in list_bins:
        liste.append(bin.show())

    return (len(liste),liste)