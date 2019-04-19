import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#load data
X = []
Y = []
for line in open('data_2d.csv'):
    x1, x2, y = line.split(',')
    fx1=float(x1)
    fx2=float(x2)
    X.append([1, fx1, fx2])
    Y.append(float(y))


#convert into numpy array

X = np.array(X)
Y = np.array(Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], Y)
plt.show()
