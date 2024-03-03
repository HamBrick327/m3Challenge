import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

## import the data into the script
file = read_csv("./data.csv")

''''''''' MODEL 1 '''''''''
##### SEATTLE #######
x = file["Year"].tolist()
print("got ", x, " from datafile",)

y = file["DeltaUnits"].tolist()
print("got ", y, "from datafile")

## make the polynomial;
z = np.polyfit(x, y, 2)
f = np.poly1d(z) ## -->
print(f)

## calculate then append the projected numbers to the lists
x.append(x[-1] + 12)
x.append(x[-1] + 10)
x.append(x[-1] + 30)
y.append(f(x[-3]))
y.append(f(x[-2]))
y.append(f(x[-1]))

## calculate new x's and y's
newY = f(x)

## display the x and y lists for debugging purposes 
print(x)
print(y)

## plot the data to return the image
plt.plot(x,y,'o') ## plot the points at the original funciton
plt.plot(x, newY) ## plot the new function
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()

#### ALBUQUERQUE ####
## reset the variables to re-do all of that for Albuquerque
y = file["NMDeltaUnits"].tolist()
x = file["Year"].tolist()


z = np.polyfit(x, y, 2)
f = np.poly1d(z)
print(f)

x.append(x[-1] + 12)
x.append(x[-1] + 10)
x.append(x[-1] + 30)
y.append(f(x[-3]))
y.append(f(x[-2]))
y.append(f(x[-1]))

## calculate new y according to x
newY = f(x)

## display the x and y lists for debugging purposes
print(x)
print(y)

## plot data... again
plt.plot(x, y, 'rx')
plt.plot(x, newY, 'g')
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show() ## <-- pauses here until you close the window
