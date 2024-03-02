import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

file = read_csv("./data.csv", usecols=['Year', 'DeltaUnits'])
x = file["Year"].tolist()
print("got ", x, " from datafile",)

y = file["DeltaUnits"].tolist()
print("got ", y, "from datafile")

## fix the first element so that the best fit line doesn't freak out
y.pop(0)
x.pop(0)
print(x)
print(y)

## make the polynomial;
z = np.polyfit(x, y, 1)
print("Z:", z)
f = np.poly1d(z)
print("f", f)

## calculate new x's and y's
newY = f(x)

## plot the data to return the image
plt.plot(x,y,'o')
plt.plot(x, newY)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()
