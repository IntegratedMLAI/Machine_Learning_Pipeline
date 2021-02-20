import matplotlib.pyplot as plt
import random

X = [x/10.0 for x in range(100)]
Y = [2.0 * x ** 2 + (random.random() - 0.5) * 2 * x for x in X]

plt.scatter(X, Y)
plt.title('This Is The Title')
plt.xlabel('These Are The X Values')
plt.ylabel('These Are The Y Values')
plt.show()

with open('./1_Fake_Data_Simple_Modeling/non_linear_data.csv', 'w') as f:
    for i in range(len(X)):
        this_line = f'{X[i]}, {Y[i]}\n'
        f.write(this_line)
