import numpy as np
import math

coordSet = set()
r = 50 #sphere radius
calcs = 300 #number of calculations to perform

def plot():
    totalCalcs = 0 #total number of calculations
    totalNumber = 0 #number of blocks plotted
    for t in np.arange(0, 2 * math.pi, 2 * math.pi / calcs):
        for u in np.arange(-r, r, 2 * math.pi / calcs):
            x = int(round(math.sqrt(r**2 - u**2) * math.cos(t)))
            y = int(round(math.sqrt(r**2 - u**2) * math.sin(t)))
            z = int(round(u))
            totalCalcs += 1
            if (x, y, z) not in coordSet: #performs faster than using len(coordSet)!!
                coordSet.add((x, y, z))
                totalNumber += 1      
                print(str(totalCalcs) + " Calculations " + str(totalNumber) + " Blocks plotted", end="\r", flush=True)
    print(str(totalCalcs) + " Calculations " + str(totalNumber) + " Blocks plotted")
    return coordSet