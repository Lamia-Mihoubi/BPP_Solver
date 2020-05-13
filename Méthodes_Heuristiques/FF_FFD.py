# First-fit Algorithm
from Functions import Bin
def first_fit(list_items, max_size):
    """ Returns list of bins with input items inside. """
    list_bins = []
    list_bins.append(Bin())  # Add first empty bin to list

    for item in list_items:
        # Go through bins and try to allocate
        alloc_flag = False

        for bin in list_bins:
            if bin.sum() + item <= max_size:
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
    list_items = []
    for bin in list_bins:
        list_items.append(bin.show())

    return (list_items)

# First-fit Decreasing Algorithm
# Sort values into decreasing order.
# Then apply first-fit algorithm.
def first_fit_dec(list_items, max_size):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    list_items.sort(reverse=True)

    # Apply first-fit algorith
    return(first_fit(list_items, max_size))
