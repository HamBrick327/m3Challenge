import matplotlib.pyplot as plt
import numpy as np

points = np.array([(1, 1), (2, 4), (5, 8), (9, 3), (2, 6), (10, 11)])

## get the x and y
x = points[:,0]
y = points[:,1]

## make the polynomial
z = np.polyfit(x, y, 1)
f = np.poly1d(z)

## calculate new x's and y's
# x_new = np.linspace(x[0], x[-1], 50)
newY = f(x)

## plot the data to return the image
plt.plot(x,y,'o', x, newY)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()