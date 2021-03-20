import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

X = [[x/10.0 for x in range(100)], [x/20.0 for x in range(100)]]
Y = [0 for _ in range(100)]

for i in range(len(X[0])):
    # print(X[0][i], X[1][i])
    Y[i] = 2.0 * X[0][i] + \
        4.0 * X[1][i] + \
        (random.random() - 0.5) * 3
 
fig = plt.figure()
ax = plt.axes(projection='3d')
 
ax.scatter3D(X[0], X[1], Y)
ax.set_xlabel('X1 Values')
ax.set_ylabel('X2 Values')
ax.set_zlabel('Y Values')
ax.set_title('3D Plot Of Linear Fake Data')
 
plt.show()