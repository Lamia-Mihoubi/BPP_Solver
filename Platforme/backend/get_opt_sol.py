import os


def get_opt_sol(classe, nomfich):
    nomfich= nomfich[:-4]
    c = "c" + str(classe)
    if classe != 3:
        n = "n" + nomfich[1]
    else:
        n = "n3"
    directory = "../opt_whole"
    for filename in os.listdir(directory):
        if filename.endswith(c + ".txt") and filename.startswith(n):
            file = open(directory + "/" + filename, 'r')
            data = file.readlines()
            for i in range(len(data)):  # every line of the file
                l1 = data[i].split()  # split it into words
                if l1[0] == nomfich:
                    return l1[1]

    return -1

