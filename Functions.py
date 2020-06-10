# Bin Class

class Bin:
    def __init__(self):
        self.list = []

    def addItem(self, item):
        self.list.append(item)

    def removeItem(self, item):
        self.list.remove(item)

    def sum(self):
        total = 0
        for elem in self.list:
            total += elem
        return total

    def show(self):
        return self.list

def emballer(liste,n):
    sol=[]
    i = 0
    while(i<n):
        list=[]
        for j in liste:
            if (j[1]==i):
                list.append(j[0])
        sol.append(list)
        i=i+1
    return sol
def takeSecond(elem):
    return elem[1]