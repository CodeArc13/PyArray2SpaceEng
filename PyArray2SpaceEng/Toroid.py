import numpy as np
import math

coordSet = set()
r = 40 #radius or torid
r2 = 4 #radius of smaller upright circles
r3 = 64 #Half of length

#calcs = 15600 #number of calculations to perform

def plot():
    totalCalcs = 0 #total number of calculations
    totalNumber = 0 #number of blocks plotted
    for u in np.arange(0, 2 * math.pi, 2 * math.pi / 500):
        for t in np.arange(0, 2 * math.pi, 2 * math.pi / 500):
            x = int(round(math.cos(t) * (r + r2 * math.cos(u))))
            y = int(round(math.sin(t) * (r + r2 * math.cos(u))))
            z = int(round(r3 * math.sin(u)))
            totalCalcs += 1
            if (x, y, z) not in coordSet: #performs faster than using len(coordSet)!!
                coordSet.add((x, y, z))
                totalNumber += 1      
                print(str(totalCalcs) + " Calculations " + str(totalNumber) + " Blocks plotted", end="\r", flush=True)
    print(str(totalCalcs) + " Calculations " + str(totalNumber) + " Blocks plotted")
    return coordSet