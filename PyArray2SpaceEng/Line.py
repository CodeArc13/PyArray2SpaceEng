import numpy as np

coordSet = set()

def plot():
    totalCalcs = 0 #total number of calculations
    totalNumber = 0 #number of blocks plotted
    for t in np.arange(0, 20, 0.01):
        x = int(round(2 * t))
        y = int(round(1 + t))
        z = int(round(-3 + t))
        if (x, y, z) not in coordSet: #performs faster than using len(coordSet)!!
            coordSet.add((x, y, z))
            totalNumber += 1      
            print(str(totalCalcs) + " Calculations " + str(totalNumber) + " Blocks plotted", end="\r", flush=True)
    print(str(totalCalcs) + " Calculations " + str(totalNumber) + " Blocks plotted")
    return coordSet