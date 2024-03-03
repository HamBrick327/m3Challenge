import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

## import the data into the script
file = read_csv("./data.csv")

def model1():
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
    plt.show()## <-- pauses here until you close the window

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
    plt.show()

def model2():
    ###### SEATTLE ######
    x = file["EstimateYears"]

    y = file["Shomeless"]

    print(x)
    print(y)

    ## calculate bet fit, but don't extend it this time


    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)
    print(f)

    newY = f(x)

    ## plot data again again
    plt.plot(x, y, 'g+')
    plt.plot(x, newY, 'r')
    # plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.show()

    # ##### ALBUQUERQUE #####
    x = file["EstimateYears"]

    y = file["Ahomeless"]

    print(x)
    print(y)

    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)
    print(f)

    newY = f(x)

    ## plot data again again
    plt.plot(x, y, 'b+')
    plt.plot(x, newY, 'y')
    # plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.show()

def model3():
    ### ONLY FOR SEATTLE THIS TIME ### 
    x = file["Percent High Density"] ## percent of high density homes in Seattle
    y = file["Shomeless2"] ## Shomeless2 reduces the scope to play better with the script

    x = x[:4]
    y = y[:4]

    print(x)
    print(y)

    ## calculate bet fit, but don't extend it this time

    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)
    print(f)

    newY = f(x)

    ## plot data again again
    plt.plot(x, y, 'g+')
    plt.plot(x, newY, 'r')
    # plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.show()

model3()