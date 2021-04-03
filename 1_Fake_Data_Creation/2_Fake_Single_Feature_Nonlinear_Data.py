import matplotlib.pyplot as plt
import random

num_pts = 100
divider = num_pts / 10
X = [x/(divider) for x in range(num_pts)]
Y = [0.2 * x ** 2 + (random.random() - 0.5) * 2 for x in X]

plt.scatter(X, Y)
plt.title('This Is The Title')
plt.xlabel('These Are The X Values')
plt.ylabel('These Are The Y Values')
plt.show()

with open('./1_Fake_Data_Creation/non_linear_data.csv', 'w') as f:
    for i in range(len(X)):
        this_line = f'{X[i]}, {Y[i]}\n'
        f.write(this_line)
