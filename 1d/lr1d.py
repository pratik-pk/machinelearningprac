import numpy as np
import matplotlib.pyplot as plt

#load data
X=[]
Y=[]
for line in open('data_1d.csv'):
    x,y=line.split(',')
    X.append(float(x))
    Y.append(float(y))

#lets Turn X and Y in numpy array

X=np.array(X)
Y=np.array(Y)

#plot to see what it's look like
plt.scatter(X,Y)
plt.show()
denominator=X.dot(X)-X.mean()*X.sum()
a=(X.dot(Y)-Y.mean()*X.sum())/denominator
b=(Y.mean()*X.dot(X)-X.mean()*X.dot(Y))/denominator

yhat=a*X+b
plt.scatter(X,Y)
plt.plot(X,yhat)
plt.show()

