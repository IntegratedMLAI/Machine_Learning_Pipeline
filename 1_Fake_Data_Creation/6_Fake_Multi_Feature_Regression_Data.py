import matplotlib.pyplot as plt
import random

num_pts = 300
div1 = num_pts / 10
div2 = num_pts / 3
X = [[x/div1 for x in range(num_pts)], 
     [x/div2 for x in range(num_pts)]]
Y = [0 for _ in range(num_pts)]

for i in range(len(X[0])):
    Y[i] = (
        3.00 * X[0][i] ** 0.33 + 2.00 * X[1][i] ** 0.50 +
        1.50 * X[0][i] + 0.25 * X[0][i] ** 2 +
        0.50 * X[0][i] * X[1][i] + 0.10 * X[1][i] ** 3 +
        (random.random() - 0.5) * 5.0)
 
fig = plt.figure()
ax = plt.axes(projection='3d')
 
ax.scatter3D(X[0], X[1], Y)
ax.set_xlabel('X1 Values')
ax.set_ylabel('X2 Values')
ax.set_zlabel('Y Values')
ax.set_title('3D Plot Of Linear Fake Data')
 
plt.show()

with open('fake_data_regression.csv', 'w') as f:
    for i in range(len(X[0])):
        this_line = f'{X[0][i]}, {X[1][i]}, {Y[i]}\n'
        f.write(this_line)