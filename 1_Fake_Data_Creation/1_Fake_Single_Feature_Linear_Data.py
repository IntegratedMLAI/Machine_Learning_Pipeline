import matplotlib.pyplot as plt
import random

num_pts = 10000
divider = num_pts / 10
X = [x/divider for x in range(num_pts)]
Y = [2.0 * x + (random.random() - 0.5) * 2 for x in X]

print(X)
print()
print(Y)

plt.scatter(X, Y)
plt.title('This Is The Title')
plt.xlabel('These Are The X Values')
plt.ylabel('These Are The Y Values')
plt.show()

with open('./1_Fake_Data_Creation/linear_data.csv', 'w') as f:
    for i in range(len(X)):
        this_line = f'{X[i]}, {Y[i]}\n'
        f.write(this_line)
