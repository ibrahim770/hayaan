# Dividing the data into training and Testing with 8th degree polynomial
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)
pageseeds= np.random.normal(3.0,1.0,100)
purchaseAmount= np.random.normal(50.0,30.0,100)/pageseeds
#plt.scatter(pageseeds,purchaseAmount)
#plt.show()
trainx= pageseeds[:80]
testx= pageseeds[80:]
trainy= purchaseAmount[:80]
testy= purchaseAmount[80:]
#plt.scatter(trainx,trainy)
#plt.scatter(testx,testy)
#plt.show()
x=  np.array(trainx)
y= np.array(trainy)
p4= np.poly1d(np.polyfit(x,y,3))
xp= np.linspace(0,7,100)
axes= plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(x,y)
plt.plot(xp,p4(xp),c='r')
plt.show()