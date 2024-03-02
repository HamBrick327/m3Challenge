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

## fix the first element so that the best fit line doesn't freak out
y.pop(0)
x.pop(0)

## make the polynomial;
z = np.polyfit(x, y, 1)
f = np.poly1d(z) ## --> 545.4x - 1.094e+06
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
plt.plot(x,y,'o')
plt.plot(x, newY)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show() ## <-- pauses here until you close the window

#### ALBUQUERQUE ####
y = file["NMDeltaUnits"].tolist()

## make sure the script doesn't freak out with the second set of numbers
