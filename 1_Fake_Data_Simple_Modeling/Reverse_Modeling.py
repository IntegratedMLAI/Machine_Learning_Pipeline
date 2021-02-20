import matplotlib.pyplot as plt
import random

X = [x/10.0 for x in range(100)]
Y = [2.0 * x + random.random() * 1.5 for x in X]

plt.scatter(X, Y)
plt.title('This Is The Title')
plt.xlabel('These Are The X Values')
plt.ylabel('These Are The Y Values')
plt.show()

"""
    Fake Data Creation
    Modeling with Fake Data
"""


"Everybody Lies, Weapons of Math Destruction & AI Superpowers, Army of None"