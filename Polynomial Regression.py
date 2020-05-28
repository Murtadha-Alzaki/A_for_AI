import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score
# the x value represent the hour which the car was driving
# the y value represent the speed of the car at the certain time
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel= np.poly1d(np.polyfit(x,y,3))
print("the r squared is :",r2_score(y,mymodel(x)))
myline= np.linspace(1,22,100)
# here yoy can pass an time value as parameter for the mymeodel
# and it will predict the speed at that time, notice that these a
#polonomila regression and it will predict based on the above data
speed = mymodel(17)
print("THe speed is ",speed)
plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()
